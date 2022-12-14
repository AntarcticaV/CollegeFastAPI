from fastapi import FastAPI
from app.routers import group_routers, student_routers


def set_routers (app :FastAPI):
    app.include_router(group_routers.router, prefix = "/group", tags=['Group'])
    app.include_router(student_routers.router, prefix= "/student", tags=['Student'])