from fastapi import APIRouter, HTTPException
from domain.exam_model import Exam
from typing import List
from persistence.repositories.exam_repository_postgres import ExamRepositoryPostgres

exams = APIRouter()
crp = ExamRepositoryPostgres()


@exams.post('/', status_code=201)
async def add_exam(payload: Exam):
    exam_id = await crp.add_exam(payload)
    response = {
        'id': exam_id,
        **payload.dict()
    }
    return response


@exams.get('/', response_model=List[Exam])
async def index():
    return await crp.get_all_exams()


@exams.put('/{id}')
async def update_exam(id: int, payload: Exam):
    exam = await crp.get_exam_by_id(id)
    if not exam:
        raise HTTPException(status_code=404, detail="Exam not found")

    update_data = payload.dict(exclude_unset=True)
    exam_in_db = Exam(**exam)

    updated_exam = exam_in_db.copy(update=update_data)
    return await crp.update_exam(id, updated_exam)


@exams.delete('/{id}')
async def delete_exam(id: int):
    exam = await crp.get_exam_by_id(id)
    if not exam:
        raise HTTPException(status_code=404, detail="Exam not found")
    return await crp.delete_exam(id)


@exams.delete('/')
async def delete_all_exams():
    return await crp.delete_all_exams()
