from typing import List
from prisma.models import Student
from app.models.college_student import BaseStudentImput, BaseStudentOut, BaseStudentPut

class BaseStudentRepasitory:
    
    async def get_student_by_id(self, id_group : int, id_student : int) -> BaseStudentOut:
        raise NotImplementedError
    
    async def get_all_student(self) -> List[BaseStudentOut]:
        raise NotImplementedError
    
    async def get_all_student_in_group(self, id : int) -> List[BaseStudentOut]:
        raise NotImplementedError
    
    async def create_student(self, student :BaseStudentImput) ->  BaseStudentOut:
        raise NotImplementedError
    
    async def delete_student(self, id_student : int) -> BaseStudentOut:
        raise NotImplementedError
    
    async def put_student(self, int, id_student : int, student :BaseStudentPut) -> BaseStudentOut:
        raise NotImplementedError