from fastapi import APIRouter, Header, Depends
from infrastructure.db.database import Session, get_db
from application.controllers.exam_solution_controller import ExamSolutionController
from application.services.auth import auth_service
from domain.exam_solution_model import ExamSolutionPostBody, ExamSolutionDB, ExamSolutionList, ExamSolutionPatch

router = APIRouter()


@router.post("/", response_model=ExamSolutionDB, status_code=201)
async def create_exam_solution(
    exam_template_id: str,
    exam_solution: ExamSolutionPostBody,
    db: Session = Depends(get_db),
    apikey: str = Header(None),
):
    auth_service.check_api_key(apikey)
    return ExamSolutionController.create_exam_solution(db, exam_template_id, exam_solution)


@router.get("/{exam_solution_id}", response_model=ExamSolutionDB, status_code=200)
async def get_exam_solution(
    exam_template_id: str,
    exam_solution_id: str,
    db: Session = Depends(get_db),
    apikey: str = Header(None),
):
    auth_service.check_api_key(apikey)
    return ExamSolutionController.get_exam_solution(db, exam_solution_id)


@router.get("/", response_model=ExamSolutionList, status_code=200)
async def get_all_exam_solutions_by_exam_template_id(
    exam_template_id: str,
    db: Session = Depends(get_db),
    apikey: str = Header(None),
):
    auth_service.check_api_key(apikey)
    return ExamSolutionController.get_all_exam_solutions_by_exam_template_id(db, exam_template_id)
    


@router.delete("/{exam_solution_id}", response_model=dict, status_code=200)
async def delete_exam_solution(
    exam_template_id: str,
    exam_solution_id: str,
    db: Session = Depends(get_db),
    apikey: str = Header(None),
):
    auth_service.check_api_key(apikey)
    ExamSolutionController.delete_exam_solution(db, exam_solution_id)
    return {"message": "The exam solution {} was deleted succesfully".format(exam_solution_id)}


@router.patch("/{exam_solution_id}", response_model=ExamSolutionDB, status_code=200)
async def update_exam_solution(
    exam_template_id: str,
    exam_solution_id: str,
    exam_solution: ExamSolutionPatch,
    db: Session = Depends(get_db),
    apikey: str = Header(None),
):

    auth_service.check_api_key(apikey)
    return ExamSolutionController.update_exam_solution(db, exam_solution_id, exam_solution)
