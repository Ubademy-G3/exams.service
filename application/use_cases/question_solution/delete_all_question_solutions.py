from persistence.repositories.question_solution_repository_postgres import QuestionSolutionRepositoryPostgres

etrp = QuestionSolutionRepositoryPostgres()

async def delete_all_question_solutions():
    return await etrp.delete_all_question_solutions()