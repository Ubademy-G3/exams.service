from persistence.repositories.exam_template_repository_postgres import ExamTemplateRepositoryPostgres
from application.serializers.exam_template_serializer import ExamTemplateSerializer
from domain.exam_template_model import ExamTemplate

etrp = ExamTemplateRepositoryPostgres()

async def add_exam_template(args):
    new_exam_template = ExamTemplate(
        name = args.name,
        course_id = args.course_id
    )
    await etrp.add_exam_template(new_exam_template)
    return ExamTemplateSerializer.serialize(new_exam_template)