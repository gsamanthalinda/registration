from pydantic import BaseModel

class Teacher(BaseModel):
    name: str
    age: int
    email: str
    department: str
    employee_id: int