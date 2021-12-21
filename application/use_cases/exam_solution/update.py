from persistence.repositories.exam_solution_repository_postgres import ExamSolutionRepositoryPostgres
from exceptions.http_exception import NotFoundException
from application.serializers.exam_solution_serializer import ExamSolutionSerializer
from exceptions.ubademy_exception import NegativeExamSolutionScoreException
import logging

logger = logging.getLogger(__name__)

esrp = ExamSolutionRepositoryPostgres()


def update_exam_solution(db, exam_solution_id, new_args):

    if new_args.score is not None and new_args.score < 0:
        raise NegativeExamSolutionScoreException(new_args.score)

    exam_solution_to_update = esrp.get_exam_solution(db, exam_solution_id)
    if not exam_solution_to_update:
        raise NotFoundException("Exam solution {}".format(exam_solution_id))

    if new_args.corrector_id is not None:
        exam_solution_to_update.corrector_id = new_args.corrector_id

    if new_args.graded is not None:
        exam_solution_to_update.graded = new_args.graded

    if new_args.score is not None:
        exam_solution_to_update.score = new_args.score

    if new_args.approval_state is not None:
        exam_solution_to_update.approval_state = new_args.approval_state

    logger.debug("Update exam solution %s", exam_solution_id)
    esrp.update_exam_solution(db)
    logger.info("Exam solution updated")
    return ExamSolutionSerializer.serialize(exam_solution_to_update)
