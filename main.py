import logging
import logging.config
import os
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi import HTTPException
from infrastructure.routes import (
    exam_template_router,
    exam_solution_router,
    question_template_router,
    question_solution_router,
    exam_solution_outside_router,
)

from infrastructure.db.database import Base, engine, DATABASE_URL
from sqlalchemy.exc import SQLAlchemyError
from exceptions.ubademy_exception import UbademyException
from exceptions.auth_exception import AuthorizationException

logging_conf_path = os.path.join(os.path.dirname(__file__), "logging.ini")
logging.config.fileConfig(logging_conf_path, disable_existing_loggers=False)


if DATABASE_URL is not None:
    Base.metadata.create_all(engine)

app = FastAPI(title="ubademy-examsservice", description="Exams service API")


@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    message = {"message": exc.detail}
    logging.error(f"status_code: {exc.status_code} message: {exc.detail}")
    return JSONResponse(status_code=exc.status_code, content=message)


@app.exception_handler(UbademyException)
async def ubademy_exception_hanlder(request, exc):
    message = {"message": exc.detail}
    logging.error(f"status_code: {exc.status_code} message: {exc.detail}")
    return JSONResponse(status_code=exc.status_code, content=message)


@app.exception_handler(AuthorizationException)
async def auth_exception_handler(request, exc):
    message = {"message": exc.detail}
    logging.error(f"status_code: {exc.status_code} message: {exc.detail}")
    return JSONResponse(status_code=exc.status_code, content=message)


@app.exception_handler(SQLAlchemyError)
async def sql_exception_handler(request, exc):
    message = {"message": str(exc.__dict__)}
    logging.critical(f"status_code: 500 message: {str(exc.__dict__)}")
    return JSONResponse(status_code=500, content=message)


@app.exception_handler(Exception)
async def unknown_exception_handler(request, exc):
    message = {"message": str(exc.__dict__)}
    logging.error(f"status_code: 500 message: {str(exc.__dict__)}")
    return JSONResponse(status_code=500, content=message)


app.include_router(exam_template_router.router, prefix="/exams", tags=["exam-templates"])

app.include_router(question_template_router.router, prefix="/exams/{exam_template_id}/questions", tags=["question-templates"])

app.include_router(exam_solution_router.router, prefix="/exams/{exam_template_id}/solutions", tags=["exam-solutions"])

app.include_router(exam_solution_outside_router.router, prefix="/exams/solutions", tags=["exam-solutions-user"])

app.include_router(
    question_solution_router.router,
    prefix="/exams/{exam_template_id}/solutions/{exam_solution_id}/answers",
    tags=["question-solutions"],
)
