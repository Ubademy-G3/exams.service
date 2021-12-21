from application.use_cases.exam_solution import create, get, delete, update


class ExamSolutionController:
    @classmethod
    def create_exam_solution(self, db, exam_template_id, args):
        return create.add_exam_solution(db, exam_template_id, args)

    @classmethod
    def get_exam_solution(self, db, exam_solution_id):
        return get.get_exam_solution(db, exam_solution_id)

    @classmethod
    def get_all_exam_solutions_by_user_id(self, db, user_id, graded, approval_state):
        return get.get_all_exam_solutions_by_user_id(db, user_id, graded, approval_state)

    @classmethod
    def get_all_exam_solutions_by_exam_template_id(self, db, exam_template_id, graded, approval_state):
        return get.get_all_exam_solutions_by_exam_template_id(db, exam_template_id, graded, approval_state)

    @classmethod
    def get_all_exam_solutions_by_corrector_id(self, db, corrector_id, graded, approval_state):
        return get.get_all_exam_solutions_by_corrector_id(db, corrector_id, graded, approval_state)

    @classmethod
    def get_all_exam_solutions_by_course_id(self, db, course_id, graded, approval_state):
        return get.get_all_exam_solutions_by_course_id(db, course_id, graded, approval_state)

    @classmethod
    def get_all_exam_solutions_by_user_id_and_course_id(self, db, user_id, course_id, graded, approval_state):
        return get.get_all_exam_solutions_by_user_id_and_course_id(db, user_id, course_id, graded, approval_state)

    @classmethod
    def get_all_exam_solutions_by_corrector_id_and_course_id(self, db, corrector_id, course_id, graded, approval_state):
        return get.get_all_exam_solutions_by_corrector_id_and_course_id(db, corrector_id, course_id, graded, approval_state)

    @classmethod
    def delete_exam_solution(self, db, exam_solution_id):
        return delete.delete_exam_solution(db, exam_solution_id)

    @classmethod
    def update_exam_solution(self, db, exam_solution_id, payload):
        return update.update_exam_solution(db, exam_solution_id, payload)
