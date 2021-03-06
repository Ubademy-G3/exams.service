from infrastructure.db.exam_solution_schema import ExamSolution


class ExamSolutionSerializer:
    @classmethod
    def serialize(self, exam_solution: ExamSolution):
        return {
            "id": exam_solution.id,
            "course_id": exam_solution.course_id,
            "user_id": exam_solution.user_id,
            "exam_template_id": exam_solution.exam_template_id,
            "graded": exam_solution.graded,
            "score": exam_solution.score,
            "max_score": exam_solution.max_score,
            "approval_state": exam_solution.approval_state,
            "corrector_id": exam_solution.corrector_id,
        }
