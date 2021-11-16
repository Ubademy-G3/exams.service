from persistence.repositories.exam_solution_repository_postgres import ExamSolutionRepositoryPostgres
from exeptions.http_exeption import NotFoundExeption

etrp = ExamSolutionRepositoryPostgres()

async def get_exam_solution(exam_solution_id):
    exam_solution = await etrp.get_exam_solution(exam_solution_id)
    if exam_solution is None:
        raise NotFoundExeption("Exam solution {}".format(exam_solution_id))
    return exam_solution