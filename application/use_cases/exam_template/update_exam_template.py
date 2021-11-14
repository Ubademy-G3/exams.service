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
    '''
    if new_args.name is not None:
        exam_template_in_db.name = new_args.name
        
    if new_args.description is not None:
        exam_template_in_db.description = new_args.description

    if new_args.category is not None:
        exam_template_in_db.category = new_args.category
        
    if new_args.kind is not None:
        exam_template_in_db.kind = new_args.kind
        
    if new_args.subscription_type is not None:
        exam_template_in_db.subscription_type = new_args.subscription_type

    if new_args.location is not None:
        exam_template_in_db.location = new_args.location
    '''
    update_data = exam_template_in_db.dict(exclude_unset=True)
    updated_exam_template = exam_template_in_db.copy(update=update_data)
    await etrp.update_exam_template(exam_template_id, updated_exam_template)
    return ExamTemplateSerializer.serialize(updated_exam_template)