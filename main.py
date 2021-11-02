from fastapi import FastAPI
from infrastructure.routes import (exam_template_router, exam_solution_router, question_template_router, question_solution_router)
from infrastructure.db.database import database, engine
from infrastructure.db.exam_template_schema import metadata

metadata.create_all(engine)

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(question_template_router.router, prefix='/api/v1/question_templates', tags=['question_templates'])

app.include_router(question_solution_router.router, prefix='/api/v1/question_solutions', tags=['question_solutions'])

app.include_router(exam_template_router.router, prefix='/api/v1/exam_templates', tags=['exam_templates'])

app.include_router(exam_solution_router.router, prefix='/api/v1/exam_solutions', tags=['exam_solutions'])
