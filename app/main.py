from fastapi import FastAPI
from .database import init_db
from .routers import student, teacher, course

app = FastAPI(
    title="students",
    docs_url="/docs",
)
init_db()

app.include_router(student.router)
app.include_router(teacher.router)
app.include_router(course.router)


@app.get("/")
def home():
    return {"message": "Welcome to my API server"}
