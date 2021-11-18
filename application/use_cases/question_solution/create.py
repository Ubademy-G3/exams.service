from persistence.repositories.question_solution_repository_postgres import QuestionSolutionRepositoryPostgres
from application.serializers.question_solution_serializer import QuestionSolutionSerializer
from infrastructure.db.question_solution_schema import QuestionSolution
from uuid import uuid4

etrp = QuestionSolutionRepositoryPostgres()

def add_question_solution(db, args):
    new_question_solution = QuestionSolution(
        id = uuid4(),
        exam_id = args.exam_id,
        question = args.question,
        type = args.type,
        options = args.options,
        correct = args.correct,
        user_id = args.user_id,
        answer = args.answer
    )
    etrp.add_question_solution(db, new_question_solution)
    return QuestionSolutionSerializer.serialize(new_question_solution)