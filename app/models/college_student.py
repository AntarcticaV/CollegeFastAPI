import datetime
from prisma.models import Group, Student
from pydantic import BaseModel
from core.prisma import prismaBD

class BaseStudent(BaseModel):
    
    first_name : str
    last_name : str
    age : int
    birth_date : datetime.datetime
    login : str
    

class BaseStudentImput(BaseStudent):
    
    group_id :int
    password : str

class BaseStudentPut(BaseStudent):
    
    group_id :int
    password : str

class BaseStudentOut(BaseStudent):
    
    id : int
    group: str | None
    group_id :int

    @staticmethod
    async def convert(orig: Student | None):
        ret = BaseStudentOut(
            id=orig.id,
            first_name=orig.first_name,
            last_name=orig.last_name,
            age=orig.age,
            birth_date=orig.birth_date,
            login=orig.login,
            group_id = orig.group_id,
            group=orig.group.name,
        )
        return ret