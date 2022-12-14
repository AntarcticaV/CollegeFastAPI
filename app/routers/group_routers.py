from typing import List
import uuid
from fastapi import APIRouter, Depends
from app.dependencies import get_group_repo
from app.repasitories.group import BaseGroupRepasitory
from app.models.college_group import BaseGroupInput, BaseGroupPut, BaseGroupOut


router = APIRouter()

@router.get("/get_by_id_group", response_model=BaseGroupOut)
async def get_by_id_group(id: int, group_repo : BaseGroupRepasitory = Depends(get_group_repo)):
    return await group_repo.get_by_id_group(id)

@router.get("/get_all_group", response_model=List[BaseGroupOut])
async def get_all_group(group_repo : BaseGroupRepasitory = Depends(get_group_repo)):
    return await group_repo.get_all_group()

@router.post("/creat_group", response_model=BaseGroupOut)
async def crear_group(group : BaseGroupInput, group_repo : BaseGroupRepasitory = Depends(get_group_repo)):
    return await group_repo.create_group(group)

@router.delete("/delete_group", response_model= BaseGroupOut)
async def delete_group(id:int, group_repo : BaseGroupRepasitory = Depends(get_group_repo)):
    return await group_repo.delete_group(id)

@router.put("/put_group", response_model=BaseGroupOut)
async def put_group(id:int, name: BaseGroupPut, group_repo : BaseGroupRepasitory = Depends(get_group_repo)):
    return await group_repo.put_group(id, name)