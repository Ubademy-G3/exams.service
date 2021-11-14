from persistence.repositories.exam_template_repository_postgres import ExamTemplateRepositoryPostgres
from errors.http_error import NotFoundError

etrp = ExamTemplateRepositoryPostgres()

async def get_exam_template(exam_template_id):
    exam_template = await etrp.get_exam_template(exam_template_id)
    if exam_template is None:
        raise NotFoundError("Exam template {}".format(exam_template_id))
    return exam_template