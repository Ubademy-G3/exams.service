from persistence.repositories.question_solution_repository_postgres import QuestionSolutionRepositoryPostgres
from exceptions.http_exception import NotFoundException
import logging

logger = logging.getLogger(__name__)

qsrp = QuestionSolutionRepositoryPostgres()


def delete_question_solution(db, question_solution_id):
    question_solution = qsrp.get_question_solution(db, question_solution_id)

    if not question_solution:
        logger.warning("Question solution %s not found", question_solution_id)
        raise NotFoundException("Question solution {}".format(question_solution_id))
    return qsrp.delete_question_solution(db, question_solution)
