from persistence.repositories.exam_template_repository_postgres import ExamTemplateRepositoryPostgres
from exeptions.http_exeption import NotFoundExeption
from application.serializers.exam_template_serializer import ExamTemplateSerializer

etrp = ExamTemplateRepositoryPostgres()

async def update_exam_template(db, exam_template_id, new_args):
    
    exam_template_to_update = await etrp.get_exam_template(db, exam_template_id)
    if not exam_template_to_update:
        raise NotFoundExeption("Exam template {}".format(exam_template_id))

    if new_args.name is not None:
        exam_template_to_update.name = new_args.name
        
    if new_args.active is not None:
        exam_template_to_update.active = new_args.active
    
    await etrp.update_exam_template(db)
    return ExamTemplateSerializer.serialize(exam_template_to_update)