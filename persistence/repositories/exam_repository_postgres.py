from domain.exam_model import Exam
from infrastructure.db.database import database
from infrastructure.db.exam_schema import exams
from domain.exam_repository import ExamRepository


class ExamRepositoryPostgres(ExamRepository):

    async def add_exam(self, payload: Exam):
        query = exams.insert().values(**payload.dict())
        return await database.execute(query=query)

    async def get_all_exams(self):
        query = exams.select()
        return await database.fetch_all(query=query)

    async def get_exam_by_id(self, id: int):
        query = exams.select(exams.c.id == id)
        return await database.fetch_one(query=query)

    async def update_exam(self, id: int, payload: Exam):
        query = (exams.update().
                 where(exams.c.id == id)
                 .values(**payload.dict()))
        return await database.execute(query=query)

    async def delete_exam(self, id: int):
        query = exams.delete().where(exams.c.id == id)
        return await database.execute(query=query)

    async def delete_all_exams(self):
        query = exams.delete()
        return await database.execute(query=query)
