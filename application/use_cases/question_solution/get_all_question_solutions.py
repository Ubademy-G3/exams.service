from persistence.repositories.question_solution_repository_postgres import QuestionSolutionRepositoryPostgres

etrp = QuestionSolutionRepositoryPostgres()

async def get_all_question_solutions():
    return await etrp.get_all_question_solutions()
