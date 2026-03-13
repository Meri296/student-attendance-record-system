# Student Attendance Record System

## Project Description
The **Student Attendance Record System** is a web-based application developed using **Django**.  
The system allows administrators and teachers to manage courses, students, and attendance records efficiently.  

The platform provides authentication for users and ensures that only authorized users can perform CRUD operations. Teachers can register, log in, and manage attendance for students enrolled in their assigned courses.

---

## Features

### Admin Features
- Admin login through the Django admin panel
- Add and manage courses
- Add and manage students
- View attendance records
- Assign students to specific courses

### Teacher Features
- Teacher registration
- Teacher login and logout
- View assigned courses
- Take attendance for students in their courses
- View attendance reports

### API Endpoints
The system also provides API endpoints for testing and data retrieval.

- `/api/students/` – Retrieve all students
- `/api/courses/` – Retrieve all courses
- `/api/attendance/` – Retrieve attendance records

These endpoints can be tested using **Postman**.

---

## Technologies Used

- Python
- Django
- HTML / CSS
- SQLite Database
- Django Authentication System
- Postman (for API testing)

---

## System Workflow

1. Admin logs into the system.
2. Admin creates courses.
3. Admin registers students and assigns them to courses.
4. Teachers register and log in to the system.
5. Teachers view their assigned courses.
6. Teachers take attendance for students.
7. Attendance records are stored in the database.
8. Attendance reports can be viewed by teachers and administrators.

---
