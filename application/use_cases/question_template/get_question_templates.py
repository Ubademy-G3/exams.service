from persistence.repositories.question_template_repository_postgres import QuestionTemplateRepositoryPostgres
from errors.http_error import NotFoundError

etrp = QuestionTemplateRepositoryPostgres()

async def get_question_templates(question_template_id):
    question_templates = await etrp.get_question_templates(question_template_id)
    if question_templates is None:
        raise NotFoundError("Question template {}".format(question_template_id))
    return question_templates