from fastapi import FastAPI
from routers.student import router as student_router
from routers.teacher import router as teacher_router
from routers.course import router as course_router

app = FastAPI()

app.include_router(student_router)
app.include_router(teacher_router)
app.include_router(course_router)
