from fastapi import APIRouter, Header, Depends
from infrastructure.db.database import Session, get_db
from application.controllers.exam_solution_controller import ExamSolutionController
from application.services.auth import auth_service
from domain.exam_solution_model import CourseExamSolutionList

router = APIRouter()


@router.get("/", response_model=CourseExamSolutionList, status_code=200)
async def get_all_exam_solutions_by_course_id(
    course_id: str,
    db: Session = Depends(get_db),
    apikey: str = Header(None),
):
    auth_service.check_api_key(apikey)
    return ExamSolutionController.get_all_exam_solutions_by_user_id(db, course_id)
