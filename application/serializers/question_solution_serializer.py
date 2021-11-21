from infrastructure.db.question_solution_schema import QuestionSolution


class QuestionSolutionSerializer:
    @classmethod
    def serialize(self, question_solution: QuestionSolution):
        return {
            "id": question_solution.id,
            "exam_solution_id": question_solution.exam_solution_id,
            "question_template_id": question_solution.question_template_id,
            "answer": question_solution.answer,
            "score": question_solution.score,
        }
