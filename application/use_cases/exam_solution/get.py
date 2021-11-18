from persistence.repositories.exam_solution_repository_postgres import ExamSolutionRepositoryPostgres
from exeptions.http_exeption import NotFoundExeption
from application.serializers.exam_solution_serializer import ExamSolutionSerializer

etrp = ExamSolutionRepositoryPostgres()

def get_exam_solution(exam_solution_id):
    exam_solution = etrp.get_exam_solution(exam_solution_id)
    if exam_solution is None:
        raise NotFoundExeption("Exam solution {}".format(exam_solution_id))
    return ExamSolutionSerializer.serialize(exam_solution)

async def exam_solution_exists(db, exam_solution_id):
    return etrp.get_exam_solution(db, exam_solution_id)