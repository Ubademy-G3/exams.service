from persistence.repositories.question_template_repository_postgres import QuestionTemplateRepositoryPostgres

etrp = QuestionTemplateRepositoryPostgres()

async def get_question_templates(id):
    return await etrp.get_question_templates(id)
