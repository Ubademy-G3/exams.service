from persistence.repositories.question_template_repository_postgres import QuestionTemplateRepositoryPostgres
from infrastructure.db.question_template_schema import QuestionTypeEnum
from exceptions.http_exception import NotFoundException
from exceptions.ubademy_exception import (InvalidQuestionTypeException, EmptyOptionListException,
                                          EmptyCorrectException, NonPositiveValueException)
from application.serializers.question_template_serializer import QuestionTemplateSerializer

qtrp = QuestionTemplateRepositoryPostgres()


def update_question_template(db, question_template_id, new_args):

    if (new_args.question_type is not None and new_args.question_type not in ["multiple_choice", "written", "media"]):
        raise InvalidQuestionTypeException(new_args.question_type)
    if (args.question_type is not None and args.question_type == "multiple_choice" and args.options is None):
        raise EmptyOptionListException()
    if (args.question_type is not None and args.question_type == "multiple_choice" and args.correct is None):
        raise EmptyCorrectException()
    if (args.value is not None and args.value <= 0):
        raise NonPositiveValueException(args.value)

    question_template_to_update = qtrp.get_question_template(db, question_template_id)
    if not question_template_to_update:
        raise NotFoundException("Question template {}".format(question_template_id))

    if new_args.question is not None:
        question_template_to_update.question = new_args.question

    if new_args.question_type is not None:
        question_template_to_update.question_type = QuestionTypeEnum.multiple_choice
        if(new_args.question_type == "written"):
            question_template_to_update.question_type = QuestionTypeEnum.written
        if(new_args.question_type == "media"):
            question_template_to_update.question_type = QuestionTypeEnum.media

    if new_args.options is not None:
        question_template_to_update.options = new_args.options

    if new_args.correct is not None:
        question_template_to_update.correct = new_args.correct

    if new_args.value is not None:
        question_template_to_update.value = new_args.value

    qtrp.update_question_template(db)
    return QuestionTemplateSerializer.serialize(question_template_to_update)
