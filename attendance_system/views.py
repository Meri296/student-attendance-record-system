from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.db.models import Count

from .models import Student, Course, Attendance
from .serializers import (
    RegisterSerializer,
    StudentSerializer,
    CourseSerializer,
    AttendanceSerializer
)
from .permissions import IsAdminOrTeacher


# ========================
# Register
# ========================
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]


# ========================
# Login
# ========================
@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username=username, password=password)

    if user:
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})

    return Response({'error': 'Invalid credentials'}, status=400)


# ========================
# Student CRUD
# ========================
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]


# ========================
# Course CRUD
# ========================
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]


# ========================
# Attendance CRUD
# ========================
class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [IsAdminOrTeacher]

    def perform_create(self, serializer):
        serializer.save(marked_by=self.request.user)

    def get_queryset(self):
        queryset = Attendance.objects.all()

        student_id = self.request.query_params.get('student')
        course_id = self.request.query_params.get('course')
        date = self.request.query_params.get('date')

        if student_id:
            queryset = queryset.filter(student_id=student_id)

        if course_id:
            queryset = queryset.filter(course_id=course_id)

        if date:
            queryset = queryset.filter(date=date)

        return queryset


# ========================
# Attendance Percentage
# ========================
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def attendance_percentage(request, student_id):
    total = Attendance.objects.filter(student_id=student_id).count()
    present = Attendance.objects.filter(
        student_id=student_id,
        status='PRESENT'
    ).count()

    percentage = (present / total) * 100 if total > 0 else 0

    return Response({
        "student_id": student_id,
        "attendance_percentage": round(percentage, 2)
    })