from domain.question_solution_model import *
from application.use_cases.question_solution.add_question_solution import add_question_solution
from application.use_cases.question_solution.get_question_solutions import get_question_solutions
from application.use_cases.question_solution.delete_question_solutions import delete_question_solutions

class QuestionSolutionController:
    @classmethod
    async def create_question_solution(self, args):
        return await add_question_solution(args)

    @classmethod
    async def get_question_solutions(self, question_solution_id):
        return await get_question_solutions(question_solution_id)

    @classmethod
    async def delete_question_solutions(self, question_solution_id):
        return await delete_question_solutions(question_solution_id)