from fastapi import APIRouter, Header, Depends
from typing import List, Optional
from infrastructure.db.database import Session, get_db
from application.controllers.exam_solution_controller import *
from application.services.auth import auth_service
from domain.exam_solution_model import *

router = APIRouter()

@router.post('/', response_model=ExamSolutionDB, status_code = 201)
async def create_exam_solution(
                                exam_solution: ExamSolutionSchema,
                                db: Session = Depends(get_db),
                                apikey: str = Header(None)
                            ):
    auth_service.check_api_key(apikey)
    return ExamSolutionController.create_exam_solution(db, exam_solution)

@router.get('/{exam_solution_id}', response_model=ExamSolutionDB, status_code = 200)
async def get_exam_solution(
                            exam_solution_id: str,
                            db: Session = Depends(get_db),
                            apikey: str = Header(None)
                        ):
    auth_service.check_api_key(apikey)
    return ExamSolutionController.get_exam_solution(db, id)

@router.delete('/{exam_solution_id}', response_model= dict, status_code = 200)
async def delete_exam_solution(
                                exam_solution_id: str,
                                db: Session = Depends(get_db),
                                apikey: str = Header(None)
                            ):
    auth_service.check_api_key(apikey)
    deleted_exam_solution = ExamSolutionController.delete_exam_solution(db, id)
    return {
        "message": "The exam solution {} was deleted succesfully".format(exam_solution_id)
    }

@router.patch('/{exam_solution_id}', response_model = ExamSolutionDB, status_code = 200)
async def update_exam_solution(
                        exam_solution_id: str,
                        exam_solution: ExamSolutionPatch,
                        db: Session = Depends(get_db),
                        apikey: str = Header(None)
                    ):

    auth_service.check_api_key(apikey)
    return ExamSolutionController.update_exam_solution(db, id, exam_solution)