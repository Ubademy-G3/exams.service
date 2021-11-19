from persistence.repositories.question_solution_repository_postgres import QuestionSolutionRepositoryPostgres
from exeptions.http_exeption import NotFoundExeption
from application.serializers.question_solution_serializer import QuestionSolutionSerializer

qsrp = QuestionSolutionRepositoryPostgres()

def update_question_solution(db, question_solution_id, new_args):
    
    question_solution_to_update = qsrp.get_question_solution(db, question_solution_id)
    if not question_solution_to_update:
        raise NotFoundExeption("Question solution {}".format(question_solution_id))

    if new_args.answer is not None:
        question_solution_to_update.answer = new_args.answer
        
    if new_args.score is not None:
        question_solution_to_update.score = new_args.score
    
    qsrp.update_question_solution(db)
    return QuestionSolutionSerializer.serialize(updated_question_solution)