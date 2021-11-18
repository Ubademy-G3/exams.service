from persistence.repositories.question_solution_repository_postgres import QuestionSolutionRepositoryPostgres
from exeptions.http_exeption import NotFoundExeption
from application.serializers.question_solution_serializer import QuestionSolutionSerializer

etrp = QuestionSolutionRepositoryPostgres()

def get_question_solutions(db, question_solution_id):
    question_solutions = etrp.get_question_solutions(db, question_solution_id)
    if question_solutions is None:
        raise NotFoundExeption("Question solution {}".format(question_solution_id))
    return question_solutions