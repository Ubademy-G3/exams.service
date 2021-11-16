from persistence.repositories.exam_template_repository_postgres import ExamTemplateRepositoryPostgres
from exeptions.http_exeption import NotFoundExeption

etrp = ExamTemplateRepositoryPostgres()

async def get_exam_template(exam_template_id):
    exam_template = await etrp.get_exam_template(exam_template_id)
    if exam_template is None:
        raise NotFoundExeption("Exam template {}".format(exam_template_id))
    return exam_template