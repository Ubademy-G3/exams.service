from domain.question_solution_model import QuestionSolution
from application.use_cases.question_solution import *

class QuestionSolutionController:
    @classmethod
    async def create_question_solution(self, args):
        return await add_question_solution(new_question_solution)

    @classmethod
    async def get_question_solution(self, question_solution_id):
        return await get_question_solution(question_solution_id)

    @classmethod
    async def delete_question_solution(self, question_solution_id):
        return await delete_question_solution(question_solution_id)