from fastapi import APIRouter
from ..schemas.course import Course
from ..services import course as course_service

router = APIRouter(prefix="/courses", tags=["courses"])


@router.post("/")
def create_course(course: Course):
    course_service.create_course(
        course.title, course.description, course.credits, course.teacher_id, course.course_code
    )
    return {"message": "course created", "course": course}


@router.get("/", response_model=list[Course])
def list_courses():
    return course_service.get_all_courses()


@router.get("/{course_id}", response_model=Course)
def course_details(course_id: int):
    course = course_service.get_course_by_id(course_id)
    return course


@router.put("/{course_id}")
def update_course(course_id: int, course: Course):
    course_service.update_course(
        course_id, course.title, course.description, course.credits, course.teacher_id, course.course_code
    )
    return {"message": "course updated", "course": course}


@router.delete("/{course_id}")
def delete_course(course_id: int):
    course_service.delete_course(course_id)
    return {"message": "course deleted"}
