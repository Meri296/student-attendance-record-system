from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login

from .models import Course, Student, Attendance
from .forms import StudentForm
from django.contrib.auth.decorators import login_required


# Take Attendance
def take_attendance(request, course_id):

    course = get_object_or_404(Course, id=course_id)
    students = Student.objects.filter(course=course)

    if request.method == "POST":
        for student in students:
            status = request.POST.get(str(student.id))

            if status:
                Attendance.objects.create(
                    student=student,
                    course=course,
                    status=status
                )

        return redirect("attendance_success")

    return render(request, "take_attendance.html", {
        "course": course,
        "students": students
    })


@login_required
def teacher_courses(request):

    # Show only courses belonging to logged-in teacher
    courses = Course.objects.filter(teacher=request.user)

    return render(request, "teacher_courses.html", {
        "courses": courses
    })


# Delete Student
def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    student.delete()
    return redirect('student_list')


# Edit Student
def edit_student(request, student_id):

    student = get_object_or_404(Student, id=student_id)

    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)

        if form.is_valid():
            form.save()
            return redirect('student_list')

    else:
        form = StudentForm(instance=student)

    return render(request, "edit_student.html", {"form": form})


# Teacher Login
def teacher_login(request):

    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_teacher:
            login(request, user)
            return redirect("teacher_dashboard")

    return render(request, "login.html")


# Student Report
def student_report(request, student_id):

    student = get_object_or_404(Student, id=student_id)

    total = Attendance.objects.filter(student=student).count()

    present = Attendance.objects.filter(
        student=student,
        status="present"
    ).count()

    percentage = (present / total * 100) if total > 0 else 0

    return render(request, "student_report.html", {
        "student": student,
        "total": total,
        "present": present,
        "percentage": percentage
    })