from fastapi import APIRouter, Header, Depends
from infrastructure.db.database import Session, get_db
from application.controllers.question_template_controller import QuestionTemplateController
from application.services.auth import auth_service
from domain.question_template_model import (
    QuestionTemplatePostBody,
    QuestionTemplateDB,
    QuestionTemplateList,
    QuestionTemplatePatch,
)
import logging

logger = logging.getLogger(__name__)

router = APIRouter()


@router.post("/", response_model=QuestionTemplateDB, status_code=201)
async def create_question_template(
    exam_template_id: str,
    question_template: QuestionTemplatePostBody,
    db: Session = Depends(get_db),
    apikey: str = Header(None),
):
    logger.debug("Creating question template for exam %s ...", exam_template_id)
    auth_service.check_api_key(apikey)
    return QuestionTemplateController.create_question_template(db, exam_template_id, question_template)


@router.get("/{question_template_id}", response_model=QuestionTemplateDB, status_code=200)
async def get_question_template(
    exam_template_id: str,
    question_template_id: str,
    db: Session = Depends(get_db),
    apikey: str = Header(None),
):
    auth_service.check_api_key(apikey)
    return QuestionTemplateController.get_question_template(db, question_template_id)


@router.get("/", response_model=QuestionTemplateList, status_code=200)
async def get_all_question_templates_by_exam_template_id(
    exam_template_id: str,
    db: Session = Depends(get_db),
    apikey: str = Header(None),
):
    auth_service.check_api_key(apikey)
    return QuestionTemplateController.get_all_question_templates_by_exam_template_id(db, exam_template_id)


@router.delete("/{question_template_id}", response_model=dict, status_code=200)
async def delete_question_template(
    exam_template_id: str,
    question_template_id: str,
    db: Session = Depends(get_db),
    apikey: str = Header(None),
):
    auth_service.check_api_key(apikey)
    QuestionTemplateController.delete_question_template(db, question_template_id)
    return {"message": "The question template {} was deleted successfully".format(question_template_id)}


@router.patch("/{question_template_id}", response_model=QuestionTemplateDB, status_code=200)
async def update_question_template(
    exam_template_id: str,
    question_template_id: str,
    question_template: QuestionTemplatePatch,
    db: Session = Depends(get_db),
    apikey: str = Header(None),
):

    auth_service.check_api_key(apikey)
    return QuestionTemplateController.update_question_template(db, question_template_id, question_template)
