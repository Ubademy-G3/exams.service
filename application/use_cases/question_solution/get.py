from persistence.repositories.question_solution_repository_postgres import QuestionSolutionRepositoryPostgres
from exceptions.http_exception import NotFoundException
from application.serializers.question_solution_serializer import QuestionSolutionSerializer
import logging

logger = logging.getLogger(__name__)

qsrp = QuestionSolutionRepositoryPostgres()


def get_question_solution(db, question_solution_id):
    question_solution = qsrp.get_question_solution(db, question_solution_id)
    if question_solution is None:
        logger.debug("Question solution %s not found", question_solution_id)
        raise NotFoundException("Question solution {}".format(question_solution_id))
    return QuestionSolutionSerializer.serialize(question_solution)


def get_all_question_solutions_by_question_template_id(db, question_template_id):
    question_solutions = qsrp.get_all_question_solutions_by_question_template_id(db, question_template_id)
    # if question_solutions is None or len(question_solutions) == 0:
    #    raise NotFoundException("Question solutions by question_template_id {}".format(question_template_id))
    question_solution_list = []
    for question_solution in question_solutions:
        question_solution_list.append(QuestionSolutionSerializer.serialize(question_solution))
    amount = len(question_solution_list)
    total_score = 0
    average_score = 0
    if amount != 0:
        for question_solution in question_solution_list:
            total_score += question_solution["score"]
        average_score = total_score/amount
    return {
        "question_template_id": question_template_id,
        "amount": amount,
        "Average": average_score,
        "question_solutions": question_solution_list,
    }


def get_all_question_solutions_by_exam_solution_id(db, exam_solution_id):
    question_solutions = qsrp.get_all_question_solutions_by_exam_solution_id(db, exam_solution_id)
    question_solution_list = []
    for question_solution in question_solutions:
        question_solution_list.append(QuestionSolutionSerializer.serialize(question_solution))
    total_score = 0
    for question_solution in question_solution_list:
        total_score += question_solution["score"]
    return {
        "exam_solution_id": exam_solution_id,
        "amount": len(question_solution_list),
        "total_score": total_score,
        "question_solutions": question_solution_list,
    }
