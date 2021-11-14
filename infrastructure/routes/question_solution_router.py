from fastapi import APIRouter, HTTPException
from typing import List
from application.controllers.question_solution_controller import *

router = APIRouter()

@router.post('/', response_model=QuestionSolution, status_code = 201)
async def create_question_solution(question_solution: QuestionSolutionSchema):
    return await QuestionSolutionController.create_question_solution(question_solution)

@router.get('/{id}', response_model=QuestionSolution, status_code = 200)
async def get_question_solution(id: str):
    return await QuestionSolutionController.get_question_solutions(id)

@router.delete('/{id}')
async def delete_question_solution(id: str):
    return await QuestionSolutionController.delete_question_solutions(id)
