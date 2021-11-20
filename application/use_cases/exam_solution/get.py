from persistence.repositories.exam_solution_repository_postgres import ExamSolutionRepositoryPostgres
from exceptions.http_exception import NotFoundException
from application.serializers.exam_solution_serializer import ExamSolutionSerializer

esrp = ExamSolutionRepositoryPostgres()


def get_exam_solution(db, exam_solution_id):
    exam_solution = esrp.get_exam_solution(db, exam_solution_id)
    if exam_solution is None:
        raise NotFoundException("Exam solution {}".format(exam_solution_id))
    return ExamSolutionSerializer.serialize(exam_solution)


def get_all_exam_solutions_by_user_id(db, user_id):
    exam_solutions = esrp.get_all_exam_solutions_by_user_id(db, user_id)
    if exam_solutions is None or len(exam_solutions) == 0:
        raise NotFoundException("Exam solutions by user_id {}".format(user_id))
    exam_solution_list = []
    for exam_solution in exam_solutions:
        exam_solution_list.append(ExamSolutionSerializer.serialize(exam_solution))
    return exam_solution_list


def get_all_exam_solutions_by_exam_template_id(db, exam_template_id):
    exam_solutions = esrp.get_all_exam_solutions_by_exam_template_id(db, exam_template_id)
    if exam_solutions is None or len(exam_solutions) == 0:
        raise NotFoundException("Exam solutions by exam_template_id {}".format(exam_template_id))
    exam_solution_list = []
    for exam_solution in exam_solutions:
        exam_solution_list.append(ExamSolutionSerializer.serialize(exam_solution))
    return exam_solution_list


def exam_solution_exists(db, exam_solution_id):
    return esrp.get_exam_solution(db, exam_solution_id)
