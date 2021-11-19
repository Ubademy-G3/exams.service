from persistence.repositories.exam_solution_repository_postgres import ExamSolutionRepositoryPostgres
from exeptions.http_exeption import NotFoundExeption

esrp = ExamSolutionRepositoryPostgres()

def delete_exam_solution(db, exam_solution_id):
    exam_solution = esrp.get_exam_solution(db, exam_solution_id)
    if not exam_solution:
        raise NotFoundExeption("Exam solution {}".format(exam_solution_id))
    return  esrp.delete_exam_solution(db, exam_solution_id)