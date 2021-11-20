from persistence.repositories.exam_template_repository_postgres import ExamTemplateRepositoryPostgres
from exeptions.http_exeption import NotFoundExeption
from application.serializers.exam_template_serializer import ExamTemplateSerializer

etrp = ExamTemplateRepositoryPostgres()


def update_exam_template(db, exam_template_id, new_args):

    exam_template_to_update = etrp.get_exam_template(db, exam_template_id)
    if not exam_template_to_update:
        raise NotFoundExeption("Exam template {}".format(exam_template_id))

    if new_args.name is not None:
        exam_template_to_update.name = new_args.name

    if new_args.state is not None:
        exam_template_to_update.state = new_args.state

    if new_args.max_score is not None:
        exam_template_to_update.max_score = new_args.max_score

    if new_args.has_multiple_choice is not None:
        exam_template_to_update.has_multiple_choice = new_args.has_multiple_choice

    if new_args.has_written is not None:
        exam_template_to_update.has_written = new_args.has_written

    if new_args.has_media is not None:
        exam_template_to_update.has_media = new_args.has_media

    etrp.update_exam_template(db)
    return ExamTemplateSerializer.serialize(exam_template_to_update)
