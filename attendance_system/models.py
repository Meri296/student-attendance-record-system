from django.db import models
from django.contrib.auth.models import AbstractUser


# Custom User Model
class User(AbstractUser):
    is_teacher = models.BooleanField(default=False)


# Course Model
class Course(models.Model):
    name = models.CharField(max_length=200)
    teacher = models.ForeignKey(
    User,
    on_delete=models.CASCADE,
    limit_choices_to={'is_teacher': True}
)
    def __str__(self):
        return self.name


# Student Model
class Student(models.Model):
    name = models.CharField(max_length=200)
    student_id = models.CharField(max_length=20, unique=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# Attendance Model
class Attendance(models.Model):

    STATUS_CHOICES = (
        ('present', 'Present'),
        ('absent', 'Absent'),
    )

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def total_present(self):
        return Attendance.objects.filter(
            student=self.student,
            status='present'
        ).count()

    def total_absent(self):
        return Attendance.objects.filter(
            student=self.student,
            status='absent'
        ).count()

    def __str__(self):
        return f"{self.student.name} - {self.status}"