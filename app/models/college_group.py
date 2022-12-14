from pydantic import BaseModel
from typing import List
from prisma.models import Group, Student

class BaseGroupInput(BaseModel):
    
    name : str
    
class BaseGroupOut(BaseModel):
    
    id : int
    name : str
    
    @staticmethod
    async def convert(orig: Group | None):
        ret = BaseGroupOut(
            id = orig.id,
            name=orig.name,
        )
        return ret
    
class BaseGroupPut(BaseModel):
    
    name : str