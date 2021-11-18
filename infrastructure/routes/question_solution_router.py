from fastapi import APIRouter, Header, Depends
from typing import List, Optional
from infrastructure.db.database import Session, get_db
from application.controllers.question_solution_controller import *
from application.services.auth import auth_service
from domain.question_solution_model import *

router = APIRouter()

@router.post('/', response_model=QuestionSolutionDB, status_code = 201)
async def create_question_solution(exam_id: str,
                                question_solution: QuestionSolutionSchema,
                                db: Session = Depends(get_db),
                                apikey: Optional[str] = Header(None)):
    auth_service.check_api_key(apikey)
    return QuestionSolutionController.create_question_solution(db, question_solution)

@router.get('/{exam_solution_id}', response_model=QuestionSolutionList, status_code = 200)
async def get_question_solutions(exam_id: str,
                                exam_solution_id: str,
                                db: Session = Depends(get_db),
                                apikey: Optional[str] = Header(None)):
    auth_service.check_api_key(apikey)
    question_solution_list = QuestionSolutionController.get_question_solutions(db, exam_solution_id)
    return {"amount": len(question_solution_list),
            "exam_solution_id": exam_solution_id,
            "question_solutions": question_solution_list}


@router.delete('/{question_solution_id}', response_model = dict, status_code = 200)
async def delete_question_solutions(exam_id: str,
                                question_solution_id: str,
                                db: Session = Depends(get_db),
                                apikey: Optional[str] = Header(None)):
    auth_service.check_api_key(apikey)
    deleted_question_solution = QuestionSolutionController.delete_question_solutions(db, question_solution_id)
    return {
        "message": "The question solution {} was deleted succesfully".format(question_solution_id)
    }