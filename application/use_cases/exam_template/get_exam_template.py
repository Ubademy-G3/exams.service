from persistence.repositories.exam_template_repository_postgres import ExamTemplateRepositoryPostgres

etrp = ExamTemplateRepositoryPostgres()

async def get_exam_template(id):
    return await etrp.get_exam_template(id)
