from fastapi import APIRouter, HTTPException
from ..schemas.student import Student
from ..services import student as student_service

router = APIRouter(prefix="/students", tags=["students"])


@router.post("/")
def register_student(student: Student):
    student_service.register_student(
        student.name, student.age, student.email, student.country, student.id_number
    )
    return {"message": "student registered", "student": student}


@router.get("/", response_model=list[Student])
def list_students():
    return student_service.get_all_students()


@router.get("/{student_id}", response_model=Student)
def student_details(student_id: int):
    student = student_service.get_student_by_id(student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student


@router.put("/{student_id}")
def update_student(student_id: int, student: Student):
    student_service.update_student(
        student_id, student.name, student.age, student.email, student.country, student.id_number
    )
    return {"message": "student updated", "student": student}


@router.delete("/{student_id}")
def delete_student(student_id: int):
    student_service.delete_student(student_id)
    return {"message": "student deleted"}
