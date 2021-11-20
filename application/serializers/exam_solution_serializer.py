from infrastructure.db.exam_solution_schema import ExamSolution


class ExamSolutionSerializer:
    @classmethod
    def serialize(self, exam_solution: ExamSolution):
        return {
            "id": exam_solution.id,
            "name": exam_solution.name,
            "course_id": exam_solution.course_id,
            "user_id": exam_solution.user_id,
            "graded": exam_solution.graded,
            "score": exam_solution.score,
            "aprobal_state": exam_solution.aprobal_state,
        }
