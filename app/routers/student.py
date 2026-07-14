from fastapi import APIRouter, HTTPException
from schemas.student import Student
from services.student import add_student, get_students, update_student, delete_student

router = APIRouter()

@router.post("/students")
def register_student(student: Student):
    add_student(student.name, student.age, student.email, student.country, student.id_number)
    return {"message": "Student registered", "student": student}

@router.get("/students")
def list_students():
    students = get_students()
    return students

@router.put("/students/{student_id}")
def edit_student(student_id: int, student: Student):
    updated = update_student(student_id, student.name, student.age, student.email, student.country, student.id_number)
    if not updated:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"message": "Student updated successfully", "student": student}

@router.delete("/students/{student_id}")
def remove_student(student_id: int):
    deleted = delete_student(student_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"message": "Student deleted successfully"}
