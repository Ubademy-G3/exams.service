from persistence.repositories.question_solution_repository_postgres import QuestionSolutionRepositoryPostgres

etrp = QuestionSolutionRepositoryPostgres()

async def get_question_solutions(id):
    return await etrp.get_question_solutions(id)
