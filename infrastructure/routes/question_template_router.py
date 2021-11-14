from fastapi import APIRouter, HTTPException
from typing import List
from application.controllers.question_template_controller import *

router = APIRouter()

@router.post('/', response_model=QuestionTemplate, status_code = 201)
async def create_question_template(question_template: QuestionTemplateSchema):
    return await QuestionTemplateController.create_question_template(question_template)

@router.get('/{id}', response_model=QuestionTemplate, status_code = 200)
async def get_question_template(id: str):
    return await QuestionTemplateController.get_question_templates(id)

@router.delete('/{id}')
async def delete_question_template(id: str):
    return await QuestionTemplateController.delete_question_templates(id)
