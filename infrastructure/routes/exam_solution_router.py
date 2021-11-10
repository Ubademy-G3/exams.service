from fastapi import APIRouter, HTTPException
from typing import List
from application.controllers.exam_solution_controller import *

router = APIRouter()

@router.post('/', response_model = ExamSolution, status_code = 201)
async def create_exam_solution(exam_solution: ExamSolutionSchema):
    return await ExamSolutionController.create_exam_solution(exam_solution)

@router.get('/{id}', response_model=ExamSolution, status_code = 200)
async def get_exam_solution(id: str):
    return await ExamSolutionController.get_exam_solution(id)

@router.delete('/{id}')
async def delete_exam_solution(id: str):
    return await ExamSolutionController.delete_exam_solution(id)
