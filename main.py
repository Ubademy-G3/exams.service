from fastapi import FastAPI
import logging
from fastapi.responses import JSONResponse
from fastapi import HTTPException
from infrastructure.routes import (
    exam_template_router,
    exam_solution_router,
    question_template_router,
    question_solution_router,
    exam_user_solution_router,
)

from infrastructure.db.database import Base, engine
from sqlalchemy.exc import SQLAlchemyError
from exceptions.ubademy_exception import UbademyException
from exceptions.auth_exception import AuthorizationException

Base.metadata.create_all(engine)

app = FastAPI(title="ubademy-examsservice", description="Exams service API")


@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    exception = {"exception": exc.detail}
    logging.error(f"status_code: {exc.status_code} message: {exc.detail}")
    return JSONResponse(status_code=exc.status_code, content=exception)


@app.exception_handler(UbademyException)
async def ubademy_exception_hanlder(request, exc):
    exception = {"exception": exc.detail}
    logging.error(f"status_code: {exc.status_code} message: {exc.detail}")
    return JSONResponse(status_code=exc.status_code, content=exception)


@app.exception_handler(AuthorizationException)
async def auth_exception_handler(request, exc):
    exception = {"exception": exc.detail}
    logging.error(f"status_code: {exc.status_code} message: {exc.detail}")
    return JSONResponse(status_code=exc.status_code, content=exception)


@app.exception_handler(SQLAlchemyError)
async def sql_exception_handler(request, exc):
    error = {"message": str(exc.__dict__)}
    logging.error(f"status_code: 500 message: {str(exc.__dict__)}")
    return JSONResponse(status_code=500, content=error)


app.include_router(exam_template_router.router, prefix="/exams", tags=["exam-templates"])

app.include_router(question_template_router.router, prefix="/exams/{exam_template_id}/questions", tags=["question-templates"])

app.include_router(exam_solution_router.router, prefix="/exams/{exam_template_id}/solutions", tags=["exam-solutions"])

app.include_router(exam_user_solution_router.router, prefix="/exams/solutions/user/{user_id}", tags=["user-solutions"])

app.include_router(
    question_solution_router.router,
    prefix="/exams/{exam_template_id}/solutions/{exam_solution_id}/answers",
    tags=["question-solutions"],
)
