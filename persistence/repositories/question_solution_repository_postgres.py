from domain.question_solution_model import QuestionSolution
from infrastructure.db.database import database
from infrastructure.db.question_solution_schema import question_solutions
from domain.question_solution_repository import QuestionSolutionRepository

class QuestionSolutionRepositoryPostgres(QuestionSolutionRepository):

    async def add_question_solution(self, question_solution: QuestionSolution):
        query = question_solutions.insert().values(**question_solution.dict())
        return await database.execute(query=query)

    async def get_question_solutions(self, exam_solution_id: str):
        query = question_solutions.select(question_solutions.c.exam_id == exam_solution_id)
        return await database.fetch_all(query=query)

    async def delete_question_solutions(self, exam_solution_id: str):
        query = question_solutions.delete().where(question_solutions.c.exam_id == exam_solution_id)
        return await database.execute(query=query)
