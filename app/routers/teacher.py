from fastapi import APIRouter
from ..schemas.teacher import Teacher
from ..services import teacher as teacher_service

router = APIRouter(prefix="/teachers", tags=["teachers"])


@router.post("/")
def create_teacher(teacher: Teacher):
    teacher_service.create_teacher(
        teacher.name, teacher.age, teacher.email, teacher.department, teacher.employee_id
    )
    return {"message": "teacher created", "teacher": teacher}


@router.get("/", response_model=list[Teacher])
def list_teachers():
    return teacher_service.get_all_teachers()


@router.get("/{teacher_id}", response_model=Teacher)
def teacher_details(teacher_id: int):
    teacher = teacher_service.get_teacher_by_id(teacher_id)
    return teacher


@router.put("/{teacher_id}")
def update_teacher(teacher_id: int, teacher: Teacher):
    teacher_service.update_teacher(
        teacher_id, teacher.name, teacher.age, teacher.email, teacher.department, teacher.employee_id
    )
    return {"message": "teacher updated", "teacher": teacher}


@router.delete("/{teacher_id}")
def delete_teacher(teacher_id: int):
    teacher_service.delete_teacher(teacher_id)
    return {"message": "teacher deleted"}
