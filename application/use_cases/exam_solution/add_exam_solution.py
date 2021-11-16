from persistence.repositories.exam_solution_repository_postgres import ExamSolutionRepositoryPostgres
from application.serializers.exam_solution_serializer import ExamSolutionSerializer
from domain.exam_solution_model import ExamSolution
from uuid import uuid4

etrp = ExamSolutionRepositoryPostgres()

async def add_exam_solution(args):
    new_exam_solution = ExamSolution(
        id = uuid4(),
        name = args.name,
        course_id = args.course_id,
        user_id = args.user_id
    )
    await etrp.add_exam_solution(new_exam_solution)
    return ExamSolutionSerializer.serialize(new_exam_solution)