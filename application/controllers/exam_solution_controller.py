from fastapi import HTTPException
from domain.exam_solution_model import ExamSolution
from application.use_cases.exam_solution import *

class ExamSolutionController:
    @classmethod
    async def create_exam_solution(self, args):
        return await add_exam_solution(new_exam_solution)

    @classmethod
    async def get_exam_solution(self, exam_solution_id):
        return await get_exam_solution(exam_solution_id)
    
    @classmethod
    async def get_all_exam_solutions(self):
        return await get_all_exam_solutions()

    '''
    @classmethod
    async def update_exam_solution(self, exam_solution_id, update_args):
        return await update_exam_solution(exam_solution_id, update_exam_solution)
    '''

    @classmethod
    async def delete_exam_solution(self, exam_solution_id):
        return await delete_exam_solution(exam_solution_id)

    @classmethod
    async def delete_all_exam_solutions(self):
        return await delete_all_exam_solutions()
            