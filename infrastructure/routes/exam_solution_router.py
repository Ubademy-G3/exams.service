from fastapi import APIRouter, HTTPException
from typing import List
from application.controllers.exam_solution_controller import *
from uuid import uuid4, UUID

router = APIRouter()

@router.post('/', status_code = 201)
async def create_exam_solution(exam_solution: ExamSolution):
    return await ExamSolutionController.create_exam_solution(exam_solution)

@router.get('/', response_model=List[ExamSolution], status_code = 200)
async def get_all_exam_solutions():
    return await ExamSolutionController.get_all_exam_solutions()

@router.delete('/{id}')
async def delete_exam_solution(id: UUID):
    return await ExamSolutionController.delete_exam_solution(id)

@router.delete('/')
async def delete_all_exam_solutions():
    return await ExamSolutionController.delete_all_exam_solutions()

'''
@router.patch('/{id}', response_model = ExamSolution, status_code = 200)
async def update_exam_solution(id: UUID, exam_solution: ExamSolution):
    return await ExamSolutionController.update_exam_solution(id, exam_solution)
'''