from persistence.repositories.question_solution_repository_postgres import QuestionSolutionRepositoryPostgres
from application.serializers.question_solution_serializer import QuestionSolutionSerializer
from domain.question_solution_model import QuestionSolution
from uuid import uuid4

etrp = QuestionSolutionRepositoryPostgres()

async def add_question_solution(args):
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
    await etrp.add_question_solution(new_question_solution)
    return QuestionSolutionSerializer.serialize(new_question_solution)