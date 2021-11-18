from infrastructure.db.exam_solution_schema import ExamSolution
from sqlalchemy import func

class ExamSolutionRepositoryPostgres():

    def add_exam_solution(self, db, exam_solution):
        db.add(exam_solution)
        db.commit()

    def get_exam_solution(self, db, exam_solution_id):
        exam_solution = db.query(ExamSolution).filter(ExamSolution.id == exam_solution_id)
        return exam_solution

    def get_exam_solutions_by_exam_id(self, db, exam_template_id):
        query = db.query(ExamSolution).filter(ExamSolution.exam_id == exam_template_id)
        exam_templates = query.all()
        return exam_solutions
    
    def get_exam_solutions_by_user_id(self, db, user_id):
        query = db.query(ExamSolution).filter(ExamSolution.user_id == user_id)
        exam_templates = query.all()
        return exam_solutions
    
    def delete_exam_solution(self, db, exam_solution):
        db.delete(exam_solution)
        db.commit()

    def update_exam_solution(self, db):
        db.commit()