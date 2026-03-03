from django.db import models
from django.contrib.auth.models import AbstractUser


# ==========================
# Custom User Model
# ==========================
class User(AbstractUser):
    ROLE_CHOICES = (
        ('ADMIN', 'Admin'),
        ('TEACHER', 'Teacher'),
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


# ==========================
# Course Model
# ==========================
class Course(models.Model):
    course_name = models.CharField(max_length=255)
    course_code = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.course_name


# ==========================
# Student Model
# ==========================
class Student(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    enrollment_number = models.CharField(max_length=100, unique=True)
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='students'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name


# ==========================
# Attendance Model
# ==========================
class Attendance(models.Model):
    STATUS_CHOICES = (
        ('PRESENT', 'Present'),
        ('ABSENT', 'Absent'),
    )

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='attendance_records'
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='attendance_records'
    )
    date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    marked_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='marked_attendance'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('student', 'course', 'date')

    def __str__(self):
        return f"{self.student.full_name} - {self.date} - {self.status}"