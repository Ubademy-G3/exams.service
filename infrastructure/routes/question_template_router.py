from fastapi import APIRouter, Header, Depends
from typing import List, Optional
from infrastructure.db.database import Session, get_db
from application.controllers.question_template_controller import *
from application.services.auth import auth_service
from domain.question_template_model import *

router = APIRouter()

@router.post('/', response_model=QuestionTemplateDB, status_code = 201)
async def create_question_template(
                                exam_id: str,
                                question_template: QuestionTemplateSchema,
                                db: Session = Depends(get_db),
                                apikey: str = Header(None)):
    auth_service.check_api_key(apikey)
    return QuestionTemplateController.create_question_template(db, question_template)

@router.get('/{question_template_id}', response_model=QuestionTemplateList, status_code = 200)
async def get_question_templates(
                                exam_id: str,
                                question_template_id: str,
                                db: Session = Depends(get_db),
                                apikey: str = Header(None)):
    auth_service.check_api_key(apikey)
    return QuestionTemplateController.get_question_templates(db, question_template_id)

    question_template_list = QuestionTemplateController.get_question_templates(db, exam_template_id)
    return {"amount": len(question_template_list),
            "exam_template_id": exam_template_id,
            "question_templates": question_template_list}

@router.delete('/{question_template_id}', response_model = dict, status_code = 200)
async def delete_question_templates(
                                exam_id: str,
                                question_template_id: str,
                                db: Session = Depends(get_db),
                                apikey: str = Header(None)):
    auth_service.check_api_key(apikey)
    deleted_question_template = QuestionTemplateController.delete_question_templates(db, question_template_id)
    return {
        "message": "The question template {} was deleted succesfully".format(question_template_id)
    }
