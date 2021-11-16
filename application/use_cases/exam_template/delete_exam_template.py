from persistence.repositories.exam_template_repository_postgres import ExamTemplateRepositoryPostgres
from exeptions.http_exeption import NotFoundExeption

etrp = ExamTemplateRepositoryPostgres()

async def delete_exam_template(exam_template_id):
    exam_template = await etrp.get_exam_template(exam_template_id)
    if not exam_template:
        raise NotFoundExeption("Exam template {}".format(exam_template_id))
    return  await etrp.delete_exam_template(exam_template_id)