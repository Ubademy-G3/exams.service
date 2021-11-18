from persistence.repositories.question_template_repository_postgres import QuestionTemplateRepositoryPostgres
from exeptions.http_exeption import NotFoundExeption
from application.serializers.question_template_serializer import QuestionTemplateSerializer

etrp = QuestionTemplateRepositoryPostgres()

async def get_question_templates(db, question_template_id):
    question_templates = await etrp.get_question_templates(db, question_template_id)
    if question_templates is None:
        raise NotFoundExeption("Question template {}".format(question_template_id))
    return QuestionTemplateSerializer.serialize(question_template)

async def question_template_exists(db, question_template_id):
    return etrp.get_question_template(db, question_template_id)