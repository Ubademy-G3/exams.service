from persistence.repositories.exam_solution_repository_postgres import ExamSolutionRepositoryPostgres

etrp = ExamSolutionRepositoryPostgres()

async def get_all_exam_solutions():
    response = await etrp.get_all_exam_solutions()
    return response
