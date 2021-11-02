from persistence.repositories.question_template_repository_postgres import QuestionTemplateRepositoryPostgres

etrp = QuestionTemplateRepositoryPostgres()

async def delete_question_template(id):
    return await etrp.delete_question_template(id)
