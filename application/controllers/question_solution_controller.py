from fastapi import HTTPException
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
    async def get_all_question_solutions(self):
        return await get_all_question_solutions()

    '''
    @classmethod
    async def update_question_solution(self, question_solution_id, update_args):
        return await update_question_solution(question_solution_id, update_question_solution)
    '''

    @classmethod
    async def delete_question_solution(self, question_solution_id):
        return await delete_question_solution(question_solution_id)

    @classmethod
    async def delete_all_question_solutions(self):
        return await delete_all_question_solutions()
            