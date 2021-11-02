from persistence.repositories.exam_solution_repository_postgres import ExamSolutionRepositoryPostgres

etrp = ExamSolutionRepositoryPostgres()

async def get_exam_solution(id):
    response = await etrp.get_exam_solution(id)
    return response
