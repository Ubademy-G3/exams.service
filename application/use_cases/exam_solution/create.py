from persistence.repositories.exam_solution_repository_postgres import ExamSolutionRepositoryPostgres
from application.serializers.exam_solution_serializer import ExamSolutionSerializer
from infrastructure.db.exam_solution_schema import ExamSolution
from uuid import uuid4

esrp = ExamSolutionRepositoryPostgres()


def add_exam_solution(db, exam_template_id, args):
    new_exam_solution = ExamSolution(
        id=uuid4(),
        course_id=args.course_id,
        user_id=args.user_id,
        exam_template_id=exam_template_id,
        graded=False,
        score=None,
        approval_state=None,
        corrector_id=None,
    )
    esrp.add_exam_solution(db, new_exam_solution)
    return ExamSolutionSerializer.serialize(new_exam_solution)
