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

app.include_router(question_template_router.router, prefix='/exams/questions/templates', tags=['question-templates'])

app.include_router(question_solution_router.router, prefix='/exams/questions/solutions', tags=['question-solutions'])

app.include_router(exam_template_router.router, prefix='/exams/templates', tags=['exam-templates'])

app.include_router(exam_solution_router.router, prefix='/exams/solutions', tags=['exam-solutions'])
