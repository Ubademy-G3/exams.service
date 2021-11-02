from persistence.repositories.question_template_repository_postgres import QuestionTemplateRepositoryPostgres

etrp = QuestionTemplateRepositoryPostgres()

async def delete_all_question_templates():
    return await etrp.delete_all_question_templates()