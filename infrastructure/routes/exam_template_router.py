from fastapi import APIRouter, Header, Depends
from typing import List, Optional
from infrastructure.db.database import Session, get_db
from application.controllers.exam_template_controller import *
from application.services.auth import auth_service
from domain.exam_template_model import *

router = APIRouter()

@router.post('/', response_model=ExamTemplateDB, status_code = 201)
async def create_exam_template(
                                exam_id: str,
                                exam_template: ExamTemplateSchema,
                                db: Session = Depends(get_db),
                                apikey: Optional[str] = Header(None)
                            ):
    auth_service.check_api_key(api_key)
    return ExamTemplateController.create_exam_template(db, exam_id, exam_template)

@router.get('/{exam_id}', response_model=ExamTemplateDB, status_code = 200)
async def get_exam_template(
                                exam_id: str,
                                db: Session = Depends(get_db),
                                apikey: Optional[str] = Header(None)
                            ):
    auth_service.check_api_key(api_key)
    return ExamTemplateController.get_exam_template(db, exam_id)

@router.get('/course/{course_id}', response_model=ExamTemplateList, status_code = 200)
async def get_exam_template(
                                course_id: str,
                                db: Session = Depends(get_db),
                                apikey: Optional[str] = Header(None)
                            ):
    auth_service.check_api_key(api_key)
    exam_template_list = ExamTemplateController.get_exam_templates_from_course(db, course_id)
    return {"amount": len(exam_template_list),
            "course_id": course_id,
            "exam_templates": exam_template_list}

@router.delete('/{exam_id}', response_model = dict, status_code = 200)
async def delete_exam_template(
                                exam_id: str,
                                db: Session = Depends(get_db),
                                apikey: Optional[str] = Header(None)
                            ):
    auth_service.check_api_key(api_key)
    deleted_exam_template = ExamTemplateController.delete_exam_template(db, exam_id)
    return {
        "message": "The exam template {} was deleted successfully".format(exam_id)
    }


@router.patch('/{exam_id}', response_model = ExamTemplateDB, status_code = 200)
async def update_exam_template(
                        exam_id: str,
                        exam_template: ExamTemplatePatch,
                        db: Session = Depends(get_db),
                        apikey: Optional[str] = Header(None)
                    ):

    auth_service.check_api_key(apikey)
    return ExamTemplateController.update_exam_template(db, exam_id, exam_template)