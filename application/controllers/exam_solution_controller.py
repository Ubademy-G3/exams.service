from application.use_cases.exam_solution import (create, get, delete, update)

class ExamSolutionController:
    @classmethod
    def create_exam_solution(self, db, args):
        return add_exam_solution(args)

    @classmethod
    def get_exam_solution(self, db, exam_solution_id):
        return get_exam_solution(exam_solution_id)
    
    @classmethod
    def delete_exam_solution(self, db, exam_solution_id):
        return delete_exam_solution(exam_solution_id)
    
    @classmethod
    def update_exam_solution(self, db, exam_solution_id, payload):
        return update_exam_solution(exam_solution_id, payload)
    