from persistence.repositories.question_solution_repository_postgres import QuestionSolutionRepositoryPostgres
from exeptions.http_exeption import NotFoundExeption

etrp = QuestionSolutionRepositoryPostgres()

def delete_question_solutions(db, question_solution_id):
    question_solutions = etrp.get_question_solutions(db, question_solution_id)
    if not question_solutions:
        raise NotFoundExeption("Question solution {}".format(question_solution_id))
    return etrp.delete_question_solutions(db, question_solutions)