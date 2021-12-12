from persistence.repositories.question_solution_repository_postgres import QuestionSolutionRepositoryPostgres
from exceptions.http_exception import NotFoundException
from application.serializers.question_solution_serializer import QuestionSolutionSerializer
from exceptions.ubademy_exception import NegativeQuestionSolutionScoreException
import logging

logger = logging.getLogger(__name__)

qsrp = QuestionSolutionRepositoryPostgres()


def update_question_solution(db, question_solution_id, new_args):

    if new_args.score is not None and new_args.score < 0:
        raise NegativeQuestionSolutionScoreException(new_args.score)

    question_solution_to_update = qsrp.get_question_solution(db, question_solution_id)

    if not question_solution_to_update:
        raise NotFoundException("Question solution {}".format(question_solution_id))

    if new_args.answer is not None:
        question_solution_to_update.answer = new_args.answer

    if new_args.score is not None:
        question_solution_to_update.score = new_args.score

    logger.debug("Update question solution %s", question_solution_id)
    qsrp.update_question_solution(db)
    logger.info("Question solution updated")
    return QuestionSolutionSerializer.serialize(question_solution_to_update)
