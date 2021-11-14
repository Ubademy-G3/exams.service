from persistence.repositories.question_solution_repository_postgres import QuestionSolutionRepositoryPostgres

etrp = QuestionSolutionRepositoryPostgres()

async def delete_question_solutions(id):
    return await etrp.delete_question_solutions(id)
