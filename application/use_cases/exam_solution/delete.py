from persistence.repositories.exam_solution_repository_postgres import ExamSolutionRepositoryPostgres
from exceptions.http_exception import NotFoundException

esrp = ExamSolutionRepositoryPostgres()


def delete_exam_solution(db, exam_solution_id):
    exam_solution = esrp.get_exam_solution(db, exam_solution_id)
    if not exam_solution:
        raise NotFoundException("Exam solution {}".format(exam_solution_id))
    return esrp.delete_exam_solution(db, exam_solution_id)
