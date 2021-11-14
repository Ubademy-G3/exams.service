from persistence.repositories.question_solution_repository_postgres import QuestionSolutionRepositoryPostgres
from errors.http_error import NotFoundError

etrp = QuestionSolutionRepositoryPostgres()

async def get_question_solutions(question_solution_id):
    question_solutions = await etrp.get_question_solutions(question_solution_id)
    if question_solutions is None:
        raise NotFoundError("Question solution {}".format(question_solution_id))
    return question_solutions