from fastapi import APIRouter, Header
from typing import List, Optional
from application.controllers.question_solution_controller import *
from application.services.auth import auth_service

router = APIRouter()

@router.post('/', response_model=QuestionSolution, status_code = 201)
async def create_question_solution(exam_id: str,
                                question_solution: QuestionSolutionSchema,
                                apikey: Optional[str] = Header(None)):
    return await QuestionSolutionController.create_question_solution(question_solution)

@router.get('/{question_solution_id}', response_model=List[QuestionSolution], status_code = 200)
async def get_question_solutions(exam_id: str,
                                question_solution_id: str,
                                apikey: Optional[str] = Header(None)):
    return await QuestionSolutionController.get_question_solutions(question_solution_id)

@router.delete('/{question_solution_id}')
async def delete_question_solutions(exam_id: str,
                                question_solution_id: str,
                                apikey: Optional[str] = Header(None)):
    return await QuestionSolutionController.delete_question_solutions(question_solution_id)
