from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    RegisterView,
    login_view,
    StudentViewSet,
    CourseViewSet,
    AttendanceViewSet,
    attendance_percentage
)

router = DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'attendance', AttendanceViewSet)

urlpatterns = [
    path('auth/register/', RegisterView.as_view()),
    path('auth/login/', login_view),
    path('attendance/<int:student_id>/percentage/', attendance_percentage),
    path('', include(router.urls)),
]