from fastapi import APIRouter, HTTPException
from typing import List
from application.controllers.question_solution_controller import *
from uuid import uuid4, UUID

router = APIRouter()

@router.post('/', status_code = 201)
async def create_question_solution(question_solution: QuestionSolution):
    return await QuestionSolutionController.create_question_solution(question_solution)

@router.get('/', response_model=List[QuestionSolution], status_code = 200)
async def get_all_question_solutions():
    return await QuestionSolutionController.get_all_question_solutions()

@router.delete('/{id}')
async def delete_question_solution(id: UUID):
    return await QuestionSolutionController.delete_question_solution(id)

@router.delete('/')
async def delete_all_question_solutions():
    return await QuestionSolutionController.delete_all_question_solutions()

'''
@router.patch('/{id}', response_model = QuestionSolution, status_code = 200)
async def update_question_solution(id: UUID, question_solution: QuestionSolution):
    return await QuestionSolutionController.update_question_solution(id, question_solution)
'''