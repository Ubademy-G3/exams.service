from persistence.repositories.exam_template_repository_postgres import ExamTemplateRepositoryPostgres

etrp = ExamTemplateRepositoryPostgres()

async def delete_exam_template(id):
    return await etrp.delete_exam_template(id)
