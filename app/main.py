from fastapi import FastAPI
from pydantic import BaseModel
from database import (
    create_table, add_student, get_students, get_student, update_student, delete_student, 
    add_teacher, get_teachers, get_teacher, update_teacher, delete_teacher, 
    add_course, get_courses, get_course, update_course, delete_course
)

app = FastAPI()
create_table()

@app.get("/")
def home():
    return {"message": "Welcome to my API server"}

@app.get("/students")
def list_students_api():
    students = get_students()
    return students

@app.get("/students/{id}")
def student_details(id: int):
    student = get_student(id)
    return student

class Student(BaseModel):
    name: str
    age: int
    email: str
    country: str
    id_number: int

@app.post("/students")
def register_student(student: Student):
    add_student(student.name, student.age, student.email, student.country, student.id_number)
    return {"message": "student registered", "student": student}


@app.put("/students/{id}")
def update_student_api(id: int, student: Student):
    update_student(id, student.name, student.age, student.email, student.country, student.id_number)
    return {"message": "student updated", "student": student}


@app.delete("/students/{id}")
def delete_student_api(id: int):
    delete_student(id)
    return {"message": "student deleted"}


class Teacher(BaseModel):
    name: str
    age: int
    email: str
    department: str
    employee_id: int


@app.post("/teachers")
def create_teacher(teacher: Teacher):
    add_teacher(teacher.name, teacher.age, teacher.email, teacher.department, teacher.employee_id)
    return {"message": "teacher created", "teacher": teacher}


@app.get("/teachers")
def list_teachers_api():
    teachers = get_teachers()
    return teachers


@app.get("/teachers/{id}")
def teacher_details(id: int):
    teacher = get_teacher(id)
   
    return teacher


@app.put("/teachers/{id}")
def update_teacher_api(id: int, teacher: Teacher):
    update_teacher(id, teacher.name, teacher.age, teacher.email, teacher.department, teacher.employee_id)
    return {"message": "teacher updated", "teacher": teacher}


@app.delete("/teachers/{id}")
def delete_teacher_api(id: int):
    delete_teacher(id)
    return {"message": "teacher deleted"}


class Course(BaseModel):
    title: str
    description: str
    credits: int
    teacher_id: int
    course_code: str


@app.post("/courses")
def create_course(course: Course):
    add_course(course.title, course.description, course.credits, course.teacher_id, course.course_code)
    return {"message": "course created", "course": course}


@app.get("/courses")
def list_courses_api():
    courses = get_courses()
    return courses


@app.get("/courses/{id}")
def course_details(id: int):
    course = get_course(id)
    return course


@app.put("/courses/{id}")
def update_course_api(id: int, course: Course):
    update_course(id, course.title, course.description, course.credits, course.teacher_id, course.course_code)
    return {"message": "course updated", "course": course}


@app.delete("/courses/{id}")
def delete_course_api(id: int):
    delete_course(id)
    return {"message": "course deleted"}

