from persistence.repositories.exam_template_repository_postgres import ExamTemplateRepositoryPostgres
from exeptions.http_exeption import NotFoundExeption
from application.serializers.exam_template_serializer import ExamTemplateSerializer

etrp = ExamTemplateRepositoryPostgres()

async def get_exam_template(db, exam_template_id):
    exam_template = etrp.get_exam_template(db, exam_template_id)
    if exam_template is None:
        raise NotFoundExeption("Exam template {}".format(exam_template_id))
    return ExamTemplateSerializer.serialize(exam_template)

async def exam_template_exists(db, exam_template_id):
    return etrp.get_exam_template(db, exam_template_id)