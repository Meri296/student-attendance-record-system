from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from .models import Course, Student, Attendance


# ----------------
# Login
# ----------------
def login_view(request):

    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect("/courses/")

    return render(request, "login.html")


# ----------------
# Teacher Courses
# ----------------
@login_required
def teacher_courses(request):

    courses = Course.objects.filter(teacher=request.user)

    return render(request, "courses.html", {
        "courses": courses
    })


# ----------------
# Take Attendance
# ----------------
@login_required
def take_attendance(request, course_id):

    course = get_object_or_404(Course, id=course_id)
    students = Student.objects.filter(course=course)

    if request.method == "POST":

        for student in students:

            status = request.POST.get(str(student.id))

            Attendance.objects.create(
                student=student,
                course=course,
                status=status
            )

        return redirect("/courses/")

    return render(request, "attendance.html", {
        "course": course,
        "students": students
    })


# ----------------
# Attendance Report
# ----------------
@login_required
def attendance_report(request, course_id):

    course = get_object_or_404(Course, id=course_id)
    records = Attendance.objects.filter(course=course)

    return render(request, "report.html", {
        "records": records,
        "course": course
    })


# =========================
# API ENDPOINTS
# =========================


def student_list(request):

    students = Student.objects.all()

    data = []

    for s in students:
        data.append({
            "id": s.id,
            "name": s.name,
            "student_id": s.student_id,
            "course": s.course.course_name
        })

    return JsonResponse(data, safe=False)


def student_detail(request, id):

    try:

        s = Student.objects.get(id=id)

        data = {
            "id": s.id,
            "name": s.name,
            "student_id": s.student_id,
            "course": s.course.course_name
        }

        return JsonResponse(data)

    except Student.DoesNotExist:
        return JsonResponse({"error": "Student not found"})


def course_list(request):

    courses = Course.objects.all()

    data = []

    for c in courses:
        data.append({
            "id": c.id,
            "course_name": c.course_name,
            "teacher": c.teacher.username
        })

    return JsonResponse(data, safe=False)


def course_detail(request, id):

    try:

        c = Course.objects.get(id=id)

        data = {
            "id": c.id,
            "course_name": c.course_name,
            "teacher": c.teacher.username
        }

        return JsonResponse(data)

    except Course.DoesNotExist:
        return JsonResponse({"error": "Course not found"})


def attendance_list(request):

    records = Attendance.objects.all()

    data = []

    for r in records:
        data.append({
            "student": r.student.name,
            "course": r.course.course_name,
            "status": r.status,
            "date": r.date
        })

    return JsonResponse(data, safe=False)


def attendance_detail(request, id):

    try:

        r = Attendance.objects.get(id=id)

        data = {
            "student": r.student.name,
            "course": r.course.course_name,
            "status": r.status,
            "date": r.date
        }

        return JsonResponse(data)

    except Attendance.DoesNotExist:
        return JsonResponse({"error": "Attendance not found"})
@login_required
def attendance_page(request):

    courses = Course.objects.filter(teacher=request.user)

    selected_course = None
    students = None

    if request.method == "POST":

        course_id = request.POST.get("course")

        selected_course = Course.objects.get(id=course_id)

        students = Student.objects.filter(course=selected_course)

        if "save_attendance" in request.POST:

            for student in students:

                status = request.POST.get(str(student.id))

                Attendance.objects.create(
                    student=student,
                    course=selected_course,
                    status=status
                )

            return redirect("/courses/")

    return render(request, "attendance_page.html", {
        "courses": courses,
        "students": students,
        "selected_course": selected_course
    })
