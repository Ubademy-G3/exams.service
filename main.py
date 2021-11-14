from fastapi import FastAPI
import logging
from fastapi.responses import JSONResponse
from fastapi import HTTPException
from infrastructure.routes import (exam_template_router, exam_solution_router,
                                question_template_router, question_solution_router)
from infrastructure.db.database import database, engine
from infrastructure.db.exam_template_schema import metadata
from errors.ubademy_error import UbademyException
from errors.auth_error import AuthorizationException

metadata.create_all(engine)

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    error = {"error": exc.detail}
    logging.error(f"status_code: {exc.status_code} message: {exc.detail}")
    return JSONResponse(status_code = exc.status_code, content = error)


@app.exception_handler(UbademyException)
async def ubademy_exception_hanlder(request, exc):
    error = {"error": exc.detail}
    logging.error(f"status_code: {exc.status_code} message: {exc.detail}")
    return JSONResponse(status_code = exc.status_code, content = error)


@app.exception_handler(AuthorizationException)
async def auth_exception_handler(request, exc):
    error = {"error": exc.detail}
    logging.error(f"status_code: {exc.status_code} message: {exc.detail}")
    return JSONResponse(status_code = exc.status_code, content = error)


app.include_router(question_template_router.router, prefix='/exams/{exam_id}/questions/templates', tags=['question-templates'])

app.include_router(question_solution_router.router, prefix='/exams/{exam_id}/questions/solutions', tags=['question-solutions'])

app.include_router(exam_template_router.router, prefix='/exams/templates', tags=['exam-templates'])

app.include_router(exam_solution_router.router, prefix='/exams/{exam_id}/solutions', tags=['exam-solutions'])


#app.include_router(template_router.router, prefix='/exams/templates', tags=['exam-templates'])

