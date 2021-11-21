from persistence.repositories.question_solution_repository_postgres import QuestionSolutionRepositoryPostgres
from application.serializers.question_solution_serializer import QuestionSolutionSerializer
from infrastructure.db.question_solution_schema import QuestionSolution
from uuid import uuid4

qsrp = QuestionSolutionRepositoryPostgres()


def add_question_solution(db, exam_solution_id, args):
    new_question_solution = QuestionSolution(
        id=uuid4(),
        exam_solution_id=exam_solution_id,
        question_template_id=args.question_template_id,
        answer=args.answer,
        score=0,
    )
    qsrp.add_question_solution(db, new_question_solution)
    return QuestionSolutionSerializer.serialize(new_question_solution)
