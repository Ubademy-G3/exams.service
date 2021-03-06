from fastapi import APIRouter, Header, Depends, Query
from infrastructure.db.database import Session, get_db
from typing import Optional
from application.controllers.exam_template_controller import ExamTemplateController
from application.services.auth import auth_service
from domain.exam_template_model import (
    ExamTemplatePostBody,
    ExamTemplateDB,
    ExamTemplateList,
    CreatorExamTemplateList,
    ExamTemplatePatch,
)
import logging

logger = logging.getLogger(__name__)

router = APIRouter()


@router.post("/", response_model=ExamTemplateDB, status_code=201)
async def create_exam_template(
    exam_template: ExamTemplatePostBody,
    db: Session = Depends(get_db),
    apikey: str = Header(None),
):
    logger.debug("Creating exam template...")
    auth_service.check_api_key(apikey)
    return ExamTemplateController.create_exam_template(db, exam_template)


@router.get("/{exam_id}", response_model=ExamTemplateDB, status_code=200)
async def get_exam_template(
    exam_id: str,
    db: Session = Depends(get_db),
    apikey: str = Header(None),
):
    auth_service.check_api_key(apikey)
    return ExamTemplateController.get_exam_template(db, exam_id)


@router.get("/course/{course_id}", response_model=ExamTemplateList, status_code=200)
async def get_all_exam_templates_by_course_id(
    course_id: str,
    has_multiple_choice: Optional[bool] = Query(None),
    has_written: Optional[bool] = Query(None),
    has_media: Optional[bool] = Query(None),
    state: Optional[str] = Query(None),
    db: Session = Depends(get_db),
    apikey: str = Header(None),
):
    auth_service.check_api_key(apikey)
    return ExamTemplateController.get_all_exam_templates_by_course_id(
        db, course_id, has_multiple_choice, has_written, has_media, state
    )


@router.get("/creator/{creator_id}", response_model=CreatorExamTemplateList, status_code=200)
async def get_all_exam_templates_by_creator_id(
    creator_id: str,
    has_multiple_choice: Optional[bool] = Query(None),
    has_written: Optional[bool] = Query(None),
    has_media: Optional[bool] = Query(None),
    state: Optional[str] = Query(None),
    db: Session = Depends(get_db),
    apikey: str = Header(None),
):
    auth_service.check_api_key(apikey)
    return ExamTemplateController.get_all_exam_templates_by_creator_id(
        db, creator_id, has_multiple_choice, has_written, has_media, state
    )


@router.delete("/{exam_id}", response_model=dict, status_code=200)
async def delete_exam_template(
    exam_id: str,
    db: Session = Depends(get_db),
    apikey: str = Header(None),
):
    auth_service.check_api_key(apikey)
    ExamTemplateController.delete_exam_template(db, exam_id)
    return {"message": "The exam template {} was deleted successfully".format(exam_id)}


@router.patch("/{exam_id}", response_model=ExamTemplateDB, status_code=200)
async def update_exam_template(
    exam_id: str,
    exam_template: ExamTemplatePatch,
    db: Session = Depends(get_db),
    apikey: str = Header(None),
):

    auth_service.check_api_key(apikey)
    return ExamTemplateController.update_exam_template(db, exam_id, exam_template)
