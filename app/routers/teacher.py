from fastapi import APIRouter, HTTPException
from schemas.teacher import Teacher
from repositories.teacher import (
    add_teacher,
    get_teacher,
    get_teachers,
    update_teacher,
    delete_teacher,
)

router= APIRouter(prefix="/teachers", tags=["teachers"])

@router.get("")
def list_teachers():
    return get_teachers()

@router.post("")
def register_teacher(teacher: Teacher):
    add_teacher(teacher.name, teacher.email, course=teacher.course, teacher_id=teacher.teacher_id)
    return {"message": "Teacher registered successfully", "teacher": teacher}

@router.get("/{teachers_id}")
def teacher_detail(id: int):
    teacher = get_teacher(id)
    if not teacher:
        raise HTTPException(status_code=404, detail="Teacher not found")
    return teacher

@router.put("/{teacher_id}")
def replace_teacher(teacher: Teacher, id: int):
    updated = update_teacher(id, teacher.name, teacher.email, teacher.course, teacher.teacher_id)
    return {"message": "Teacher record updated successfully", "teacher": updated}

@router.delete("/{teacher_id}")
def remove_teacher(id: int):
    delete_teacher(id)
    return {"message": "Teacher record deleted successfully"}

