from typing import List
from prisma.models import Group, Student
from app.models.college_group import BaseGroupInput, BaseGroupPut, BaseGroupOut

class BaseGroupRepasitory:
    
    async def get_dy_id_group(self, id : int) -> BaseGroupOut:
        raise NotImplementedError
    
    async def get_all_group(self) -> List[BaseGroupOut]:
        raise NotImplementedError
    
    async def create_group(self, group :BaseGroupInput) -> BaseGroupOut:
        raise NotImplementedError
    
    async def delete_group(self, id : int) -> BaseGroupOut:
        raise NotImplementedError
    
    async def put_group(self, id : int, product :BaseGroupPut) -> BaseGroupOut:
        raise NotImplementedError