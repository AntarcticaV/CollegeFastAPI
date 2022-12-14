from typing import List
from prisma import Prisma
from prisma.models import Group, Student
from core.prisma import prismaBD
from app.repasitories.base_college_group import BaseGroupRepasitory
from app.models.college_group import BaseGroupInput, BaseGroupPut, BaseGroupOut

class GroupTmpRepasitory(BaseGroupRepasitory):
    
    async def get_by_id_group(self, id: int) -> BaseGroupOut:
        group_out = await prismaBD.group.find_first(where={'id':id})
        return await BaseGroupOut.convert(group_out)
    
    async def create_group(self, group: BaseGroupInput) -> BaseGroupOut:
        new_group = await prismaBD.group.create(data={'name':group.name})
        return BaseGroupOut.convert(new_group)
    
    async def get_all_group(self) -> List[BaseGroupOut]:
        group_out = []
        for val in await prismaBD.group.find_many():
            group_out.append(await BaseGroupOut.convert(val))
        return group_out
    
    async def delete_group(self, id:int) -> BaseGroupOut:
        delete_group = await prismaBD.group.delete(where={'id':id})
        return await BaseGroupOut.convert(delete_group)
    
    async def put_group(self, id:int, name:BaseGroupPut) -> BaseGroupOut:
        group_out = await prismaBD.group.update(where={'id':id}, data={'name':name.name})
        return await BaseGroupOut.convert(group_out)