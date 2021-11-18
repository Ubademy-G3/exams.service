from fastapi import FastAPI
import logging
from fastapi.responses import JSONResponse
from fastapi import HTTPException
from infrastructure.routes import (exam_template_router, exam_solution_router,
                                question_template_router, question_solution_router)

from infrastructure.db.database import Base, engine
from sqlalchemy.exc import SQLAlchemyError
from exeptions.ubademy_exeption import UbademyException
from exeptions.auth_exeption import AuthorizationException

Base.metadata.create_all(engine)

app = FastAPI(
                title = "ubademy-examsservice",
                description = "Exams service API"
)

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    exeption = {"exeption": exc.detail}
    logging.exeption(f"status_code: {exc.status_code} message: {exc.detail}")
    return JSONResponse(status_code = exc.status_code, content = exeption)


@app.exception_handler(UbademyException)
async def ubademy_exception_hanlder(request, exc):
    exeption = {"exeption": exc.detail}
    logging.exeption(f"status_code: {exc.status_code} message: {exc.detail}")
    return JSONResponse(status_code = exc.status_code, content = exeption)


@app.exception_handler(AuthorizationException)
async def auth_exception_handler(request, exc):
    exeption = {"exeption": exc.detail}
    logging.exeption(f"status_code: {exc.status_code} message: {exc.detail}")
    return JSONResponse(status_code = exc.status_code, content = exeption)


app.include_router(question_template_router.router, prefix='/exams/{exam_id}/questions/templates', tags=['question-templates'])

app.include_router(question_solution_router.router, prefix='/exams/{exam_id}/questions/solutions', tags=['question-solutions'])

app.include_router(exam_template_router.router, prefix='/exams/templates', tags=['exam-templates'])

app.include_router(exam_solution_router.router, prefix='/exams/{exam_id}/solutions', tags=['exam-solutions'])


#app.include_router(template_router.router, prefix='/exams/templates', tags=['exam-templates'])

