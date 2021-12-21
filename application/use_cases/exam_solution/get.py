from persistence.repositories.exam_solution_repository_postgres import ExamSolutionRepositoryPostgres
from exceptions.http_exception import NotFoundException
from application.serializers.exam_solution_serializer import ExamSolutionSerializer
import logging

logger = logging.getLogger(__name__)

esrp = ExamSolutionRepositoryPostgres()


def get_exam_solution(db, exam_solution_id):
    exam_solution = esrp.get_exam_solution(db, exam_solution_id)
    if exam_solution is None:
        logger.warning("Exam solution %s not found", exam_solution_id)
        raise NotFoundException("Exam solution {}".format(exam_solution_id))
    return ExamSolutionSerializer.serialize(exam_solution)


def get_all_exam_solutions_by_user_id(db, user_id, graded, approval_state):
    exam_solutions = esrp.get_all_exam_solutions_by_user_id(db, user_id, graded, approval_state)
    exam_solution_list = []
    for exam_solution in exam_solutions:
        exam_solution_list.append(ExamSolutionSerializer.serialize(exam_solution))
    amount = len(exam_solution_list)
    amount_graded = 0
    total_score = 0
    approval_count = 0
    average_score = 0
    approval_rate = 0
    if amount != 0:
        for exam_solution in exam_solution_list:
            if exam_solution["graded"] is True:
                amount_graded += 1
                total_score += exam_solution["score"]/exam_solution["max_score"]
                if exam_solution["approval_state"] is True:
                    approval_count += 1
    if amount_graded != 0:
        average_score = total_score/amount_graded
        approval_rate = approval_count/amount_graded
    return {
        "user_id": user_id,
        "amount": amount,
        "amount_graded": amount_graded,
        "average_score": average_score,
        "approval_rate": approval_rate,
        "exam_solutions": exam_solution_list,
    }


def get_all_exam_solutions_by_exam_template_id(db, exam_template_id, graded, approval_state):
    exam_solutions = esrp.get_all_exam_solutions_by_exam_template_id(db, exam_template_id, graded, approval_state)
    exam_solution_list = []
    for exam_solution in exam_solutions:
        exam_solution_list.append(ExamSolutionSerializer.serialize(exam_solution))
    amount = len(exam_solution_list)
    amount_graded = 0
    total_score = 0
    approval_count = 0
    average_score = 0
    approval_rate = 0
    if amount != 0:
        for exam_solution in exam_solution_list:
            if exam_solution["graded"] is True:
                amount_graded += 1
                total_score += exam_solution["score"]/exam_solution["max_score"]
                if exam_solution["approval_state"] is True:
                    approval_count += 1
    if amount_graded != 0:
        average_score = total_score/amount_graded
        approval_rate = approval_count/amount_graded
    return {
        "exam_template_id": exam_template_id,
        "amount": amount,
        "amount_graded": amount_graded,
        "average_score": average_score,
        "approval_rate": approval_rate,
        "exam_solutions": exam_solution_list,
    }


def get_all_exam_solutions_by_course_id(db, course_id, graded, approval_state):
    exam_solutions = esrp.get_all_exam_solutions_by_course_id(db, course_id, graded, approval_state)
    exam_solution_list = []
    for exam_solution in exam_solutions:
        exam_solution_list.append(ExamSolutionSerializer.serialize(exam_solution))
    amount = len(exam_solution_list)
    amount_graded = 0
    total_score = 0
    approval_count = 0
    average_score = 0
    approval_rate = 0
    if amount != 0:
        for exam_solution in exam_solution_list:
            if exam_solution["graded"] is True:
                amount_graded += 1
                total_score += exam_solution["score"]/exam_solution["max_score"]
                if exam_solution["approval_state"] is True:
                    approval_count += 1
    if amount_graded != 0:
        average_score = total_score/amount_graded
        approval_rate = approval_count/amount_graded
    return {
        "course_id": course_id,
        "amount": amount,
        "amount_graded": amount_graded,
        "average_score": average_score,
        "approval_rate": approval_rate,
        "exam_solutions": exam_solution_list,
    }


def get_all_exam_solutions_by_user_id_and_course_id(db, user_id, course_id, graded, approval_state):
    exam_solutions = esrp.get_all_exam_solutions_by_user_id_and_course_id(db, user_id, course_id, graded, approval_state)
    exam_solution_list = []
    for exam_solution in exam_solutions:
        exam_solution_list.append(ExamSolutionSerializer.serialize(exam_solution))
    amount = len(exam_solution_list)
    amount_graded = 0
    total_score = 0
    approval_count = 0
    average_score = 0
    approval_rate = 0
    if amount != 0:
        for exam_solution in exam_solution_list:
            if exam_solution["graded"] is True:
                amount_graded += 1
                total_score += exam_solution["score"]/exam_solution["max_score"]
                if exam_solution["approval_state"] is True:
                    approval_count += 1
    if amount_graded != 0:
        average_score = total_score/amount_graded
        approval_rate = approval_count/amount_graded
    return {
        "user_id": user_id,
        "course_id": course_id,
        "amount": amount,
        "amount_graded": amount_graded,
        "average_score": average_score,
        "approval_rate": approval_rate,
        "exam_solutions": exam_solution_list,
    }


def get_all_exam_solutions_by_corrector_id_and_course_id(db, corrector_id, course_id, graded, approval_state):
    exam_solutions = esrp.get_all_exam_solutions_by_corrector_id_and_course_id(
        db, corrector_id, course_id, graded, approval_state
    )
    exam_solution_list = []
    for exam_solution in exam_solutions:
        exam_solution_list.append(ExamSolutionSerializer.serialize(exam_solution))
    amount = len(exam_solution_list)
    amount_graded = 0
    total_score = 0
    approval_count = 0
    average_score = 0
    approval_rate = 0
    if amount != 0:
        for exam_solution in exam_solution_list:
            if exam_solution["graded"] is True:
                amount_graded += 1
                total_score += exam_solution["score"]/exam_solution["max_score"]
                if exam_solution["approval_state"] is True:
                    approval_count += 1
    if amount_graded != 0:
        average_score = total_score/amount_graded
        approval_rate = approval_count/amount_graded
    return {
        "corrector_id": corrector_id,
        "course_id": course_id,
        "amount": amount,
        "amount_graded": amount_graded,
        "average_score": average_score,
        "approval_rate": approval_rate,
        "exam_solutions": exam_solution_list,
    }


def get_all_exam_solutions_by_corrector_id(db, corrector_id, graded, approval_state):
    exam_solutions = esrp.get_all_exam_solutions_by_corrector_id(db, corrector_id, graded, approval_state)
    exam_solution_list = []
    for exam_solution in exam_solutions:
        exam_solution_list.append(ExamSolutionSerializer.serialize(exam_solution))
    amount = len(exam_solution_list)
    amount_graded = 0
    approval_count = 0
    approval_rate = 0
    if amount != 0:
        for exam_solution in exam_solution_list:
            if exam_solution["graded"] is True:
                amount_graded += 1
                if exam_solution["approval_state"] is True:
                    approval_count += 1
    if amount_graded != 0:
        approval_rate = approval_count/amount_graded
    return {
        "corrector_id": corrector_id,
        "amount": amount,
        "amount_graded": amount_graded,
        "approval_rate": approval_rate,
        "exam_solutions": exam_solution_list,
    }


def exam_solution_exists(db, exam_solution_id):
    return esrp.get_exam_solution(db, exam_solution_id)
