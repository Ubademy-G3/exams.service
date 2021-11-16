from fastapi import APIRouter, Header
from typing import List, Optional
from application.controllers.question_template_controller import *
from application.services.auth import auth_service

router = APIRouter()

@router.post('/', response_model=QuestionTemplate, status_code = 201)
async def create_question_template(exam_id: str,
                                question_template: QuestionTemplateSchema,
                                apikey: Optional[str] = Header(None)):
    return await QuestionTemplateController.create_question_template(question_template)

@router.get('/{question_template_id}', response_model=List[QuestionTemplate], status_code = 200)
async def get_question_templates(exam_id: str,
                                question_template_id: str,
                                apikey: Optional[str] = Header(None)):
    return await QuestionTemplateController.get_question_templates(question_template_id)

@router.delete('/{question_template_id}')
async def delete_question_templates(exam_id: str,
                                question_template_id: str,
                                apikey: Optional[str] = Header(None)):
    return await QuestionTemplateController.delete_question_templates(question_template_id)
