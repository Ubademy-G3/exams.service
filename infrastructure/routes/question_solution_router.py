from fastapi import APIRouter, Header, Depends
from infrastructure.db.database import Session, get_db
from application.controllers.question_solution_controller import QuestionSolutionController
from application.services.auth import auth_service
from domain.question_solution_model import (QuestionSolutionPostBody, QuestionSolutionDB,
                                            QuestionSolutionList, QuestionSolutionPatch)

router = APIRouter()


@router.post("/", response_model=QuestionSolutionDB, status_code=201)
async def create_question_solution(
    exam_template_id: str,
    exam_solution_id: str,
    question_solution: QuestionSolutionPostBody,
    db: Session = Depends(get_db),
    apikey: str = Header(None),
):
    auth_service.check_api_key(apikey)
    return QuestionSolutionController.create_question_solution(db, exam_solution_id, question_solution)


@router.get("/{question_solution_id}", response_model=QuestionSolutionDB, status_code=200)
async def get_question_solution(
    exam_template_id: str,
    exam_solution_id: str,
    question_solution_id: str,
    db: Session = Depends(get_db),
    apikey: str = Header(None),
):
    auth_service.check_api_key(apikey)
    return QuestionSolutionController.get_question_solution(db, question_solution_id)


"""
@router.get('/', response_model=QuestionSolutionList, status_code = 200)
async def get_all_question_solutions_by_question_template_id(
    question_template_id: str,
    db: Session = Depends(get_db),
    apikey: str = Header(None),
):
    auth_service.check_api_key(apikey)
    return QuestionSolutionController.get_all_question_solutions_by_question_template_id(db, question_template_id)
"""


@router.get("/", response_model=QuestionSolutionList, status_code=200)
async def get_all_question_solutions_by_exam_solution_id(
    exam_template_id: str,
    exam_solution_id: str,
    db: Session = Depends(get_db),
    apikey: str = Header(None),
):
    auth_service.check_api_key(apikey)
    return QuestionSolutionController.get_all_question_solutions_by_exam_solution_id(db, exam_solution_id)


@router.delete("/{question_solution_id}", response_model=dict, status_code=200)
async def delete_question_solution(
    exam_template_id: str,
    exam_solution_id: str,
    question_solution_id: str,
    db: Session = Depends(get_db),
    apikey: str = Header(None),
):
    auth_service.check_api_key(apikey)
    QuestionSolutionController.delete_question_solution(db, question_solution_id)
    return {"message": "The question solution {} was deleted successfully".format(question_solution_id)}


@router.patch("/{question_solution_id}", response_model=QuestionSolutionDB, status_code=200)
async def update_question_solution(
    exam_template_id: str,
    exam_solution_id: str,
    question_solution_id: str,
    question_solution: QuestionSolutionPatch,
    db: Session = Depends(get_db),
    apikey: str = Header(None),
):

    auth_service.check_api_key(apikey)
    return QuestionSolutionController.update_question_solution(db, question_solution_id, question_solution)
