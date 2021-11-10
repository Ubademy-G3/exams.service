from domain.exam_solution_model import ExamSolution

class ExamSolutionSerializer:

    @classmethod
    def serialize(self, exam_solution: ExamSolution):
        return {
        "id": args.id,
        "name": args.name,
        "course_id": args.course_id,
        "user_id": args.user_id,
        "graded": args.graded,
        "score": args.score,
        "aprobal_state": args.aprobal_state
    }