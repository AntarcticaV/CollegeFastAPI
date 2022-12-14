from typing import List
from prisma import Prisma
from prisma.models import Group, Student
from core.prisma import prismaBD
from app.repasitories.base_college_student import BaseStudentRepasitory
from app.models.college_student import BaseStudentImput, BaseStudentOut, BaseStudentPut

class StudentTmpRepasitory(BaseStudentRepasitory):
    
    async def get_all_student(self) -> List[BaseStudentOut]:
        student_out = []
        for val in await prismaBD.student.find_many():
            student_out.append(await BaseStudentOut.convert(val))
        return student_out
    
    async def create_student(self, student: BaseStudentImput) -> BaseStudentOut:
        student_out = await prismaBD.student.create(data={'first_name':student.first_name, 'last_name':student.last_name, 'age':student.age, 
                                                          'birth_date':student.birth_date, 'login':student.login, 'password':student.password,
                                                          'group':{"connect":{'id':student.group_id}}}, include={'group':True})
        return await BaseStudentOut.convert(student_out)
    
    async def delete_student(self, id_student: int) -> BaseStudentOut:
        delete_group = await prismaBD.student.delete(where={'id':id_student}, include={'group':True})
        return await BaseStudentOut.convert(delete_group)
    
    async def get_all_student_in_group(self, id_group: int) -> List[BaseStudentOut]:
        student_out = []
        for val in await prismaBD.student.find_many(include={'group':True}):
            if val.group_id == id_group:
                student_out.append(await BaseStudentOut.convert(val))
        return student_out
    
    async def  get_student_by_id(self, id:int):
        student_out = await prismaBD.student.find_first(where={'id':id}, include={'group':True})
        return await BaseStudentOut.convert(student_out)
    
    async def put_student(self, id_student: int, student: BaseStudentPut) -> BaseStudentOut:
        student_out = await prismaBD.student.update(where={'id':id_student}, data={'age':student.age, 'first_name':student.first_name, 'birth_date':student.birth_date,
                                                                                   'last_name':student.last_name, 'login':student.login, 'password':student.password,
                                                                                   'group_id':student.group_id}, 
                                                    include={'group':True})
        return await BaseStudentOut.convert(student_out)