from application.use_cases.question_solution import create, get, delete, update


class QuestionSolutionController:
    @classmethod
    def create_question_solution(self, db, exam_solution_id, args):
        return create.add_question_solution(db, exam_solution_id, args)

    @classmethod
    def get_question_solution(self, db, question_solution_id):
        return get.get_question_solution(db, question_solution_id)

    @classmethod
    def get_all_question_solutions_by_question_template_id(self, db, question_template_id):
        return get.get_all_question_solutions_by_question_template_id(db, question_template_id)

    @classmethod
    def get_all_question_solutions_by_exam_solution_id(self, db, exam_solution_id):
        return get.get_all_question_solutions_by_exam_solution_id(db, exam_solution_id)

    @classmethod
    def delete_question_solution(self, db, question_solution_id):
        return delete.delete_question_solution(db, question_solution_id)

    @classmethod
    def update_question_solution(self, db, question_solution_id, payload):
        return update.update_question_solution(db, question_solution_id, payload)
