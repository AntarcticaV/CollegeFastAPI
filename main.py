import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent))
from fastapi import FastAPI
import uvicorn
from core.router import set_routers
from core.prisma import prismaBD
from core import setting
from prisma.models import Group, Student



app = FastAPI(title= "Learn FastAPI")


@app.on_event("startup")
async def startup():
    await prismaBD.connect()
    set_routers(app)


@app.on_event("shutdown")
async def shutdown():
    await prismaBD.disconnect()


if __name__ == "__main__":
    uvicorn.run("main:app", port=setting.POST, host=setting.HOST, reload=True)
