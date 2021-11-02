from persistence.repositories.exam_template_repository_postgres import ExamTemplateRepositoryPostgres

etrp = ExamTemplateRepositoryPostgres()

async def get_all_exam_templates():
    return await etrp.get_all_exam_templates()
