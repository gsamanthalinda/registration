from pydantic import BaseModel
class Course(BaseModel):
    title: str
    description: str
    credits: int
    teacher_id: int
    course_code: str