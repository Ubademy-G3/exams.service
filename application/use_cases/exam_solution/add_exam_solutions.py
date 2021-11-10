from persistence.repositories.exam_solution_repository_postgres import ExamSolutionRepositoryPostgres
from application.serializers.exam_solution_serializer import ExamSolutionSerializer

etrp = ExamSolutionRepositoryPostgres()

async def add_exam_solution(args):
    new_exam_solution = ExamSolution(
        name = args.name,
        course_id = args.course_id,
        user_id = args.user_id,
        graded = args.graded,
        score = args.score,
        aprobal_state = args.aprobal_state
    )
    await etrp.add_exam_solution(exam_solution)
    return ExamSolutionSerializer.serialize(new_exam_solution)