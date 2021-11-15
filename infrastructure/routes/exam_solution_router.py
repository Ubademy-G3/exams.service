from fastapi import APIRouter, Header
from typing import List, Optional
from application.controllers.exam_solution_controller import *
from application.services.auth import auth_service

router = APIRouter()

@router.post('/', response_model=ExamSolution, status_code = 201)
async def create_exam_solution(exam_id: str,
                                exam_solution: ExamSolutionSchema,
                                apikey: Optional[str] = Header(None)):
    return await ExamSolutionController.create_exam_solution(exam_solution)

@router.get('/{exam_solution_id}', response_model=ExamSolution, status_code = 200)
async def get_exam_solution(exam_id: str,
                            exam_solution_id: str,
                            apikey: Optional[str] = Header(None)):
    return await ExamSolutionController.get_exam_solution(id)

@router.delete('/{exam_solution_id}')
async def delete_exam_solution(exam_id: str,
                                exam_solution_id: str,
                                apikey: Optional[str] = Header(None)):
    return await ExamSolutionController.delete_exam_solution(id)


@router.patch('/{exam_solution_id}', response_model = ExamSolution, status_code = 200)
async def update_exam_solution(
                        exam_id: str,
                        exam_solution_id: str,
                        exam_solution: ExamSolutionPatch,
                        apikey: Optional[str] = Header(None)
                    ):

    auth_service.check_api_key(apikey)
    return await ExamSolutionController.update_exam_solution(id, exam_solution)