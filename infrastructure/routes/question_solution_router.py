from fastapi import APIRouter, Header
from typing import List, Optional
from application.controllers.question_solution_controller import *
from application.services.auth import auth_service

router = APIRouter()

@router.post('/', response_model=QuestionSolution, status_code = 201)
async def create_question_solution(question_solution: QuestionSolutionSchema,
                                apikey: Optional[str] = Header(None)):
    return await QuestionSolutionController.create_question_solution(question_solution)

@router.get('/{id}', response_model=QuestionSolution, status_code = 200)
async def get_question_solution(id: str,
                                apikey: Optional[str] = Header(None)):
    return await QuestionSolutionController.get_question_solutions(id)

@router.delete('/{id}')
async def delete_question_solution(id: str,
                                apikey: Optional[str] = Header(None)):
    return await QuestionSolutionController.delete_question_solutions(id)
