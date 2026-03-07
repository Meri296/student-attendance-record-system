from django.urls import path
from . import views

urlpatterns = [

    path("courses/", views.teacher_courses, name="teacher_courses"),

    path('student/delete/<int:student_id>/',
         views.delete_student,
         name='delete_student'),

    path('student/edit/<int:student_id>/',
         views.edit_student,
         name='edit_student'),

    path("attendance/<int:course_id>/",
         views.take_attendance,
         name="take_attendance"),

]