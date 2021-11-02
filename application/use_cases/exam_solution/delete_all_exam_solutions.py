from persistence.repositories.exam_solution_repository_postgres import ExamSolutionRepositoryPostgres

etrp = ExamSolutionRepositoryPostgres()

async def delete_all_exam_solutions():
    response = await etrp.delete_all_exam_solutions()
    return response