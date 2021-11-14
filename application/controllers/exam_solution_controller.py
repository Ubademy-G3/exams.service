from domain.exam_solution_model import *
from application.use_cases.exam_solution.add_exam_solution import add_exam_solution
from application.use_cases.exam_solution.update_exam_solution import update_exam_solution
from application.use_cases.exam_solution.get_exam_solution import get_exam_solution
from application.use_cases.exam_solution.delete_exam_solution import delete_exam_solution

class ExamSolutionController:
    @classmethod
    async def create_exam_solution(self, args):
        return await add_exam_solution(args)

    @classmethod
    async def get_exam_solution(self, exam_solution_id):
        return await get_exam_solution(exam_solution_id)
    
    @classmethod
    async def delete_exam_solution(self, exam_solution_id):
        return await delete_exam_solution(exam_solution_id)
    
    @classmethod
    async def update_exam_solution(self, exam_solution_id, payload):
        return await update_exam_solution(exam_solution_id, payload)
    