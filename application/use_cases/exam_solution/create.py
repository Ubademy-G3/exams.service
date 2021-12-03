from persistence.repositories.exam_solution_repository_postgres import ExamSolutionRepositoryPostgres
from persistence.repositories.exam_template_repository_postgres import ExamTemplateRepositoryPostgres
from application.serializers.exam_solution_serializer import ExamSolutionSerializer
from infrastructure.db.exam_solution_schema import ExamSolution
from infrastructure.db.exam_template_schema import ExamStateEnum
from uuid import uuid4
from exceptions.ubademy_exception import (NonPositiveExamSolutionMaxScoreException, ExamSolutionTriesExceededException,
                                          ExamSolutionUsesAnInvalidTest)


esrp = ExamSolutionRepositoryPostgres()
etrp = ExamTemplateRepositoryPostgres()


def add_exam_solution(db, exam_template_id, args):

    if args.max_score <= 0:
        raise NonPositiveExamSolutionMaxScoreException(args.max_score)

    previous_exam_solutions = esrp.get_all_exam_solutions_by_user_id_and_exam_template_id(db, args.user_id, exam_template_id)

    if previous_exam_solutions is not None:
        exam_template = etrp.get_exam_template(db, exam_template_id)
        if exam_template.state != ExamStateEnum.active:
            raise ExamSolutionUsesAnInvalidTest(exam_template_id, exam_template.state)
        previous_attempts = len(previous_exam_solutions)
        if previous_attempts >= exam_template.max_attempts:
            raise ExamSolutionTriesExceededException(
                args.user_id,
                exam_template_id,
                previous_attempts,
                exam_template.max_attempts
            )

    new_exam_solution = ExamSolution(
        id=uuid4(),
        course_id=args.course_id,
        user_id=args.user_id,
        exam_template_id=exam_template_id,
        corrector_id=None,
        graded=False,
        score=None,
        max_score=args.max_score,
        approval_state=None,
    )

    esrp.add_exam_solution(db, new_exam_solution)
    return ExamSolutionSerializer.serialize(new_exam_solution)
