from persistence.repositories.exam_template_repository_postgres import ExamTemplateRepositoryPostgres
from application.serializers.exam_template_serializer import ExamTemplateSerializer
from domain.exam_template_model import ExamTemplate

etrp = ExamTemplateRepositoryPostgres()

async def delete_exam_template(exam_template_id):
    result = await etrp.delete_exam_template(exam_template_id)
    return  result