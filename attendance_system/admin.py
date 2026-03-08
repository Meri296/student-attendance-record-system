from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Course, Student, Attendance


# Custom User Admin Display
class CustomUserAdmin(UserAdmin):

    fieldsets = UserAdmin.fieldsets + (
        ('Role Information', {
            'fields': ('is_teacher',),
        }),
    )

    list_display = ('username', 'email', 'is_teacher', 'is_staff')


admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Attendance)