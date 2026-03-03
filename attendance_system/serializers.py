from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Student, Course, Attendance

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'role']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class AttendanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Attendance
        fields = '__all__'

    def validate(self, data):
        # Prevent duplicate attendance manually
        if Attendance.objects.filter(
            student=data['student'],
            course=data['course'],
            date=data['date']
        ).exists():
            raise serializers.ValidationError(
                "Attendance already marked for this student on this date."
            )
        return data