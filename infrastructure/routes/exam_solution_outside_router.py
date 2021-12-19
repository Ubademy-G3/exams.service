from fastapi import APIRouter, Header, Depends, Query
from infrastructure.db.database import Session, get_db
from typing import Optional
from application.controllers.exam_solution_controller import ExamSolutionController
from application.services.auth import auth_service
from domain.exam_solution_model import (UserExamSolutionList, CorrectorExamSolutionList,
                                        CourseExamSolutionList, UserCourseExamSolutionList)

router = APIRouter()


@router.get("/user/{user_id}/", response_model=UserExamSolutionList, status_code=200)
async def get_all_exam_solutions_by_user_id(
    user_id: str,
    graded: Optional[bool] = Query(None),
    approval_state: Optional[bool] = Query(None),
    db: Session = Depends(get_db),
    apikey: str = Header(None),
):
    auth_service.check_api_key(apikey)
    return ExamSolutionController.get_all_exam_solutions_by_user_id(db, user_id, graded, approval_state)


@router.get("/corrector/{corrector_id}/", response_model=CorrectorExamSolutionList, status_code=200)
async def get_all_exam_solutions_by_corrector_id(
    corrector_id: str,
    graded: Optional[bool] = Query(None),
    approval_state: Optional[bool] = Query(None),
    db: Session = Depends(get_db),
    apikey: str = Header(None),
):
    auth_service.check_api_key(apikey)
    return ExamSolutionController.get_all_exam_solutions_by_corrector_id(db, corrector_id, graded, approval_state)


@router.get("/course/{course_id}/", response_model=CourseExamSolutionList, status_code=200)
async def get_all_exam_solutions_by_course_id(
    course_id: str,
    graded: Optional[bool] = Query(None),
    approval_state: Optional[bool] = Query(None),
    db: Session = Depends(get_db),
    apikey: str = Header(None),
):
    auth_service.check_api_key(apikey)
    return ExamSolutionController.get_all_exam_solutions_by_course_id(db, course_id, graded, approval_state)


@router.get("/user/{user_id}/course/{course_id}/", response_model=UserCourseExamSolutionList, status_code=200)
async def get_all_exam_solutions_by_user_id_and_course_id(
    user_id: str,
    course_id: str,
    graded: Optional[bool] = Query(None),
    approval_state: Optional[bool] = Query(None),
    db: Session = Depends(get_db),
    apikey: str = Header(None),
):
    auth_service.check_api_key(apikey)
    return ExamSolutionController.get_all_exam_solutions_by_user_id_and_course_id(
        db, user_id, course_id, graded, approval_state
    )
