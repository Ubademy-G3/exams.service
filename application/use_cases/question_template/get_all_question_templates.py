from persistence.repositories.question_template_repository_postgres import QuestionTemplateRepositoryPostgres

etrp = QuestionTemplateRepositoryPostgres()

async def get_all_question_templates():
    return await etrp.get_all_question_templates()
