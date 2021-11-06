from domain.question_solution_model import QuestionSolution

class QuestionSolutionSerializer:

    @classmethod
    def serialize(self, question_solution: QuestionSolution):
        return {
        "id": args.id,
        "exam_id": args.exam_id,
        "question": args.question,
        "type": args.type,
        "options": args.options,
        "correct": args.correct,
        "user_id": args.user_id,
        "answer": args.answer
    }