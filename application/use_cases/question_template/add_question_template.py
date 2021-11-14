from persistence.repositories.question_template_repository_postgres import QuestionTemplateRepositoryPostgres
from application.serializers.question_template_serializer import QuestionTemplateSerializer
from domain.question_template_model import QuestionTemplate

etrp = QuestionTemplateRepositoryPostgres()

async def add_question_template(args):
    new_question_template = QuestionTemplate(
        exam_id = args.exam_id,
        question = args.question,
        type = args.type,
        options = args.options,
        correct = args.correct
    )
    await etrp.add_question_template(new_question_template)
    return QuestionTemplateSerializer.serialize(new_question_template)
