from persistence.repositories.exam_template_repository_postgres import ExamTemplateRepositoryPostgres
from domain.exam_template_model import *
from errors.http_error import NotFoundError
from application.serializers.exam_template_serializer import ExamTemplateSerializer

etrp = ExamTemplateRepositoryPostgres()

async def update_exam_template(exam_template_id, new_args):
    
    exam_template_to_update = await etrp.get_exam_template(exam_template_id)
    if not exam_template_to_update:
        raise NotFoundError("Exam template {}".format(exam_template_id))

    exam_template_in_db = ExamTemplate(**exam_template_to_update)

    if new_args.name is not None:
        exam_template_in_db.name = new_args.name
        
    if new_args.active is not None:
        exam_template_in_db.active = new_args.active
    
    update_data = exam_template_in_db.dict(exclude_unset=True)
    updated_exam_template = exam_template_in_db.copy(update=update_data)
    await etrp.update_exam_template(exam_template_id, updated_exam_template)
    return ExamTemplateSerializer.serialize(updated_exam_template)