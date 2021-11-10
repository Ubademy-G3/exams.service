from persistence.repositories.question_solution_repository_postgres import QuestionSolutionRepositoryPostgres
from application.serializers.question_solution_serializer import QuestionSolutionSerializer

etrp = QuestionSolutionRepositoryPostgres()

async def add_question_solution(args):
    new_question_solution = QuestionSolution(
        exam_id = args.exam_id,
        question = args.question,
        type = args.type,
        options = args.options,
        correct = args.correct,
        user_id = args.user_id,
        answer = args.answer
    )
    await etrp.add_question_solution(question_solution)
    return QuestionSolutionSerializer.serialize(new_question_solution)