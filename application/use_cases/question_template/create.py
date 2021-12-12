from persistence.repositories.question_template_repository_postgres import QuestionTemplateRepositoryPostgres
from application.serializers.question_template_serializer import QuestionTemplateSerializer
from infrastructure.db.question_template_schema import QuestionTemplate, QuestionTypeEnum
from exceptions.ubademy_exception import (InvalidQuestionTypeException, EmptyOptionListException,
                                          EmptyCorrectException, NonPositiveQuestionTemplateValueException)
from uuid import uuid4
import logging

logger = logging.getLogger(__name__)

qtrp = QuestionTemplateRepositoryPostgres()


def add_question_template(db, exam_template_id, args):

    if (args.question_type is not None and args.question_type not in ["multiple_choice", "written", "media"]):
        logger.warning("Trying to create question template %s with invalid type", exam_template_id)
        raise InvalidQuestionTypeException(args.question_type)

    if (args.question_type is not None and args.question_type == "multiple_choice" and args.options is None):
        logger.warning("Trying to create question template %s with no options", exam_template_id)
        raise EmptyOptionListException()

    if (args.question_type is not None and args.question_type == "multiple_choice" and args.correct is None):
        logger.warning("Trying to create question template %s with empty correct", exam_template_id)
        raise EmptyCorrectException()

    if (args.value is not None and args.value <= 0):
        logger.warning("Trying to create question template %s with negative or inexistent value", exam_template_id)
        raise NonPositiveQuestionTemplateValueException(args.value)

    new_question_template = QuestionTemplate(
        id=uuid4(),
        exam_id=exam_template_id,
        question=args.question,
        question_type=QuestionTypeEnum.written,
        options=args.options,
        correct=args.correct,
        value=args.value,
    )

    if(args.question_type == "multiple_choice"):
        new_question_template.question_type = QuestionTypeEnum.multiple_choice

    if(args.question_type == "media"):
        new_question_template.question_type = QuestionTypeEnum.media

    if new_question_template.value is None:
        new_question_template.value = 1

    qtrp.add_question_template(db, new_question_template)
    return QuestionTemplateSerializer.serialize(new_question_template)
