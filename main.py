from fastapi import FastAPI
from infrastructure.routes.exams import exams
from infrastructure.db.database import database, engine
from infrastructure.db.exam_schema import metadata

metadata.create_all(engine)

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(exams, prefix='/api/v1/exams', tags=['exams'])
