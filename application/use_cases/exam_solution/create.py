from persistence.repositories.exam_solution_repository_postgres import ExamSolutionRepositoryPostgres
from persistence.repositories.exam_template_repository_postgres import ExamTemplateRepositoryPostgres
from application.serializers.exam_solution_serializer import ExamSolutionSerializer
from infrastructure.db.exam_solution_schema import ExamSolution
from infrastructure.db.exam_template_schema import ExamStateEnum
from uuid import uuid4
from exceptions.ubademy_exception import (NonPositiveExamSolutionMaxScoreException, ExamSolutionTriesExceededException,
                                          ExamSolutionUsesAnInvalidTest)

import logging

logger = logging.getLogger(__name__)

esrp = ExamSolutionRepositoryPostgres()
etrp = ExamTemplateRepositoryPostgres()


def add_exam_solution(db, exam_template_id, args):

    if args.max_score <= 0:
        logger.error("Trying to create exam template %s solution with non-positive max score", exam_template_id)
        raise NonPositiveExamSolutionMaxScoreException(args.max_score)

    previous_exam_solutions = esrp.get_all_exam_solutions_by_user_id_and_exam_template_id(db, args.user_id, exam_template_id)
    previous_attempts = len(previous_exam_solutions)

    if previous_attempts > 0:
        exam_template = etrp.get_exam_template(db, exam_template_id)
        if exam_template.state != ExamStateEnum.active:
            logger.error("Trying to create exam template %s solution with invalid state", exam_template_id)
            raise ExamSolutionUsesAnInvalidTest(exam_template_id, exam_template.state)
        
        if previous_attempts >= exam_template.max_attempts:
            logger.error("Trying to create exam template %s solution exceeding attemps", exam_template_id)
            raise ExamSolutionTriesExceededException()

    new_exam_solution = ExamSolution(
        id=uuid4(),
        course_id=args.course_id,
        user_id=args.user_id,
        exam_template_id=exam_template_id,
        corrector_id=None,
        graded=False,
        score=0,
        max_score=args.max_score,
        approval_state=False,
    )

    esrp.add_exam_solution(db, new_exam_solution)
    return ExamSolutionSerializer.serialize(new_exam_solution)
