from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    # Browser pages
    path('login/', views.login_view),
    path('courses/', views.teacher_courses),
    path('attendance/<int:course_id>/', views.take_attendance),
    path('report/<int:course_id>/', views.attendance_report),

    # API endpoints
    path('api/students/', views.student_list),
    path('api/students/<int:id>/', views.student_detail),

    path('api/courses/', views.course_list),
    path('api/courses/<int:id>/', views.course_detail),

    path('api/attendance/', views.attendance_list),
    path('api/attendance/<int:id>/', views.attendance_detail),
    path('attendance/', views.attendance_page),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('register/', views.register_teacher, name="register"),
    path('login/', views.teacher_login, name="login"),
    path('logout/', views.teacher_logout, name="logout"),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    

]