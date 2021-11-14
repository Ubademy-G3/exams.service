from fastapi import APIRouter, HTTPException
from typing import List
from application.controllers.template_controller import *

router = APIRouter()

@router.post('/', response_model=ExamTemplate, status_code = 201)
async def create_exam_template(exam_template: ExamTemplateSchema):
    return await ExamTemplateController.create_exam_template(exam_template)

@router.get('/{id}', response_model=ExamTemplate, status_code = 200)
async def get_exam_template(id: str):
    return await ExamTemplateController.get_exam_template(id)

@router.delete('/{id}')
async def delete_exam_template(id: str):
    return await ExamTemplateController.delete_exam_template(id)
