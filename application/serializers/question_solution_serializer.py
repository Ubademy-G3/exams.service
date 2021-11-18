from infrastructure.db.question_solution_schema import QuestionSolution

class QuestionSolutionSerializer:

    @classmethod
    def serialize(self, question_solution: QuestionSolution):
        return {
        "id": question_solution.id,
        "exam_id": question_solution.exam_id,
        "question": question_solution.question,
        "type": question_solution.type,
        "options": question_solution.options,
        "correct": question_solution.correct,
        "user_id": question_solution.user_id,
        "answer": question_solution.answer
    }