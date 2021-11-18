from application.use_cases.question_solution import (create, get, delete)#, update)

class QuestionSolutionController:
    @classmethod
    def create_question_solution(self, db, args):
        return add_question_solution(args)

    @classmethod
    def get_question_solutions(self, db, question_solution_id):
        return get_question_solutions(question_solution_id)

    @classmethod
    def delete_question_solutions(self, db, question_solution_id):
        return delete_question_solutions(question_solution_id)