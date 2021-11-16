from persistence.repositories.question_template_repository_postgres import QuestionTemplateRepositoryPostgres
from exeptions.http_exeption import NotFoundExeption

etrp = QuestionTemplateRepositoryPostgres()

async def delete_question_templates(question_template_id):
    question_templates = await etrp.get_question_templates(question_template_id)
    if not question_templates:
        raise NotFoundExeption("Question template {}".format(question_template_id))
    return  await etrp.delete_question_templates(question_template_id)