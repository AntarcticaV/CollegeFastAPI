from typing import List
import uuid
from fastapi import APIRouter, Depends
from app.dependencies import get_student_repo
from app.repasitories.student import BaseStudentRepasitory
from app.models.college_student import BaseStudentImput, BaseStudentOut, BaseStudentPut

router = APIRouter()

@router.get("/get_all_student", response_model=List[BaseStudentOut])
async def get_all_student(student_repo:BaseStudentRepasitory = Depends(get_student_repo)):
    return await student_repo.get_all_student()

@router.get("/get_all_student_in_group", response_model=List[BaseStudentOut])
async def get_all_student_in_group(id_group:int, student_repo:BaseStudentRepasitory = Depends(get_student_repo)):
    return await student_repo.get_all_student_in_group(id_group)

@router.get('/get_student_by_id', response_model=BaseStudentOut)
async def get_student_by_id(id:int, student_repo:BaseStudentRepasitory = Depends(get_student_repo)):
    return await student_repo.get_student_by_id(id)

@router.post("/create_student", response_model=BaseStudentOut)
async def create_student(student:BaseStudentImput, student_repo:BaseStudentRepasitory = Depends(get_student_repo)):
    return await student_repo.create_student(student)

@router.delete("/delete_student", response_model=BaseStudentOut)
async def delete_student(id_student:int, student_repo:BaseStudentRepasitory = Depends(get_student_repo)):
    return await student_repo.delete_student(id_student)


@router.put('/put_student', response_model=BaseStudentOut)
async def put_student(id:int, student:BaseStudentPut,student_repo:BaseStudentRepasitory = Depends(get_student_repo)):
    return await student_repo.put_student(id, student)