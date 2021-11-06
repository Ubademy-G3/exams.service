from domain.exam_solution_model import ExamSolution
from infrastructure.db.database import database
from infrastructure.db.exam_solution_schema import exam_solutions
from domain.exam_solution_repository import ExamSolutionRepository


class ExamSolutionRepositoryPostgres(ExamSolutionRepository):

    async def add_exam_solution(self, exam_solution: ExamSolution):
        query = exam_solutions.insert().values(**exam_solution.dict())
        return await database.execute(query=query)

    async def get_all_exams(self):
        query = exam_solutions.select()
        return await database.fetch_all(query=query)

    async def get_exam_by_id(self, id: str):
        query = exam_solutions.select(exam_solutions.c.id == id)
        return await database.fetch_one(query=query)

    async def update_exam(self, id: str, payload: ExamSolution):
        query = (exam_solutions.update().
                 where(exam_solutions.c.id == id)
                 .values(**payload.dict()))
        return await database.execute(query=query)

    async def delete_exam(self, id: str):
        query = exam_solutions.delete().where(exam_solutions.c.id == id)
        return await database.execute(query=query)

    async def delete_all_exams(self):
        query = exam_solutions.delete()
        return await database.execute(query=query)
