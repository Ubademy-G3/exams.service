from persistence.repositories.question_solution_repository_postgres import QuestionSolutionRepositoryPostgres
from exeptions.http_exeption import NotFoundExeption

qsrp = QuestionSolutionRepositoryPostgres()

def delete_question_solution(db, question_solution_id):
    question_solution = qsrp.get_question_solution(db, question_solution_id)
    if not question_solution:
        raise NotFoundExeption("Question solution {}".format(question_solution_id))
    return qsrp.delete_question_solution(db, question_solution)