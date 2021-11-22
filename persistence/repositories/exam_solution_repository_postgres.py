from infrastructure.db.exam_solution_schema import ExamSolution


class ExamSolutionRepositoryPostgres:
    def add_exam_solution(self, db, exam_solution):
        db.add(exam_solution)
        db.commit()

    def get_exam_solution(self, db, exam_solution_id):
        exam_solution = db.query(ExamSolution).filter(ExamSolution.id == exam_solution_id).first()
        return exam_solution

    def get_all_exam_solutions_by_exam_template_id(self, db, exam_template_id, graded, approval_state):
        query = db.query(ExamSolution).filter(ExamSolution.exam_template_id == exam_template_id)
        if graded is not None:
            query = query.filter(ExamTemplate.graded == graded)
        if approval_state is not None:
            query = query.filter(ExamTemplate.approval_state == approval_state)
        exam_solutions = query.all()
        return exam_solutions

    def get_all_exam_solutions_by_user_id(self, db, user_id, graded, approval_state):
        query = db.query(ExamSolution).filter(ExamSolution.user_id == user_id)
        if graded is not None:
            query = query.filter(ExamTemplate.graded == graded)
        if approval_state is not None:
            query = query.filter(ExamTemplate.approval_state == approval_state)
        exam_solutions = query.all()
        return exam_solutions

    def get_all_exam_solutions_by_corrector_id(self, db, corrector_id, graded, approval_state):
        query = db.query(ExamSolution).filter(ExamSolution.corrector_id == corrector_id)
        if graded is not None:
            query = query.filter(ExamTemplate.graded == graded)
        if approval_state is not None:
            query = query.filter(ExamTemplate.approval_state == approval_state)
        exam_solutions = query.all()
        return exam_solutions

    def get_all_exam_solutions_by_course_id(self, db, course_id, graded, approval_state):
        query = db.query(ExamSolution).filter(ExamSolution.course_id == course_id)
        if graded is not None:
            query = query.filter(ExamTemplate.graded == graded)
        if approval_state is not None:
            query = query.filter(ExamTemplate.approval_state == approval_state)
        exam_solutions = query.all()
        return exam_solutions

    def delete_exam_solution(self, db, exam_solution):
        db.delete(exam_solution)
        db.commit()

    def update_exam_solution(self, db):
        db.commit()
