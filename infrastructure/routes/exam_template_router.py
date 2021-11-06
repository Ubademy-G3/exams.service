from fastapi import APIRouter, HTTPException
from typing import List
from application.controllers.exam_template_controller import *

router = APIRouter()

@router.post('/', status_code = 201)
async def create_exam_template(exam_template: ExamTemplate):
    return await ExamTemplateController.create_exam_template(exam_template)

@router.get('/{id}', response_model=ExamTemplate, status_code = 200)
async def get_exam_template(id: str):
    return await ExamTemplateController.get_exam_template(id)

@router.get('/', response_model=List[ExamTemplate], status_code = 200)
async def get_all_exam_templates():
    return await ExamTemplateController.get_all_exam_templates()

@router.delete('/{id}')
async def delete_exam_template(id: str):
    return await ExamTemplateController.delete_exam_template(id)

@router.delete('/')
async def delete_all_exam_templates():
    return await ExamTemplateController.delete_all_exam_templates()

@router.patch('/{id}', response_model = ExamTemplate, status_code = 200)
async def update_exam_template(id: str, exam_template: ExamTemplatePatch):
    return await ExamTemplateController.update_exam_template(id, exam_template)