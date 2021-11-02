from persistence.repositories.exam_template_repository_postgres import ExamTemplateRepositoryPostgres

etrp = ExamTemplateRepositoryPostgres()

async def delete_all_exam_templates():
    return await etrp.delete_all_exam_templates()