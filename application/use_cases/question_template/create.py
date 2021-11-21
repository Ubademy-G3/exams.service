from persistence.repositories.question_template_repository_postgres import QuestionTemplateRepositoryPostgres
from application.serializers.question_template_serializer import QuestionTemplateSerializer
from infrastructure.db.question_template_schema import QuestionTemplate  # (QuestionTemplate, QuestionTypeEnum)
from uuid import uuid4


# from exceptions.ubademy_exception import InvalidQuestionTypeException


qtrp = QuestionTemplateRepositoryPostgres()


def add_question_template(db, exam_template_id, args):
    # if (args.type not in ["multiple choice", "written", "media"]):
    #    raise InvalidQuestionTypeException()
    new_question_template = QuestionTemplate(
        id=uuid4(),
        exam_id=exam_template_id,
        question=args.question,
        is_written=args.is_written,
        is_media=args.is_media,
        options=args.options,
        correct=args.correct,
        value=args.value,
        # type = args.type,#QuestionTypeEnum.multiple_choice,
    )
    # if(args.type == "written"):
    #    new_question_template.type = QuestionTypeEnum.written
    # if(args.type == "media"):
    #    new_question_template.type = QuestionTypeEnum.media

    if new_question_template.is_written is None:
        new_question_template.is_written = False
    if new_question_template.is_media is None:
        new_question_template.is_media = False
    if new_question_template.is_written is None:
        new_question_template.options = {}
    if new_question_template.is_written is None:
        new_question_template.correct = 0
    if new_question_template.is_written is None:
        new_question_template.value = 1

    qtrp.add_question_template(db, new_question_template)
    return QuestionTemplateSerializer.serialize(new_question_template)
