from persistence.repositories.question_template_repository_postgres import QuestionTemplateRepositoryPostgres
from exceptions.http_exception import NotFoundException
from application.serializers.question_template_serializer import QuestionTemplateSerializer

qtrp = QuestionTemplateRepositoryPostgres()


def update_question_template(db, question_template_id, new_args):

    question_template_to_update = qtrp.get_question_template(db, question_template_id)
    if not question_template_to_update:
        raise NotFoundException("Question template {}".format(question_template_id))

    if new_args.question is not None:
        question_template_to_update.question = new_args.question

    if new_args.is_written is not None:
        question_template_to_update.is_written = new_args.is_written

    if new_args.is_media is not None:
        question_template_to_update.is_media = new_args.is_media

    if new_args.options is not None:
        question_template_to_update.options = new_args.options

    if new_args.correct is not None:
        question_template_to_update.correct = new_args.correct

    if new_args.value is not None:
        question_template_to_update.value = new_args.value

    qtrp.update_question_template(db)
    return QuestionTemplateSerializer.serialize(question_template_to_update)
