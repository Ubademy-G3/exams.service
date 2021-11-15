from fastapi import APIRouter, Header
from typing import List, Optional
from application.controllers.exam_template_controller import *
from application.services.auth import auth_service

router = APIRouter()

@router.post('/', response_model=ExamTemplate, status_code = 201)
async def create_exam_template(exam_template: ExamTemplateSchema,
                                apikey: Optional[str] = Header(None)):
    return await ExamTemplateController.create_exam_template(exam_template)

@router.get('/{exam_id}', response_model=ExamTemplate, status_code = 200)
async def get_exam_template(exam_id: str,
                                apikey: Optional[str] = Header(None)):
    return await ExamTemplateController.get_exam_template(exam_id)

@router.delete('/{exam_id}')
async def delete_exam_template(exam_id: str,
                                apikey: Optional[str] = Header(None)):
    return await ExamTemplateController.delete_exam_template(exam_id)


@router.patch('/{exam_id}', response_model = ExamTemplate, status_code = 200)
async def update_exam_template(
                        exam_id: str,
                        exam_template: ExamTemplatePatch,
                        apikey: Optional[str] = Header(None)
                    ):

    auth_service.check_api_key(apikey)
    return await ExamTemplateController.update_exam_template(exam_id, exam_template)