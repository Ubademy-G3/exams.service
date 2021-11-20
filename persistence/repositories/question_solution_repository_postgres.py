from infrastructure.db.question_solution_schema import QuestionSolution


class QuestionSolutionRepositoryPostgres:
    def add_question_solution(self, db, question_solution):
        db.add(question_solution)
        db.commit()

    def get_question_solution(self, db, question_solution_id):
        question_solution = db.query(QuestionSolution).filter(QuestionSolution.id == question_solution_id).first()
        return question_solution

    def get_all_question_solutions_by_question_template_id(self, db, question_template_id):
        query = db.query(QuestionSolution).filter(QuestionSolution.question_template_id == question_template_id)
        question_solutions = query.all()
        return question_solutions

    def get_all_question_solutions_by_exam_solution_id(self, db, exam_solution_id):
        query = db.query(QuestionSolution).filter(QuestionSolution.exam_solution_id == exam_solution_id)
        question_solutions = query.all()
        return question_solutions

    def delete_question_solution(self, db, question_solution):
        db.delete(question_solution)
        db.commit()

    def update_exam_solution(self, db):
        db.commit()
