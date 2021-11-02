from persistence.repositories.exam_solution_repository_postgres import ExamSolutionRepositoryPostgres

etrp = ExamSolutionRepositoryPostgres()

async def delete_exam_solution(id):
    response = await etrp.delete_exam_solution(id)
    return response