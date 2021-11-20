from persistence.repositories.question_template_repository_postgres import QuestionTemplateRepositoryPostgres
from application.serializers.question_template_serializer import QuestionTemplateSerializer
from infrastructure.db.question_template_schema import QuestionTemplate  # (QuestionTemplate, QuestionTypeEnum)
from exeptions.ubademy_exeption import InvalidQuestionTypeException
from uuid import uuid4

qtrp = QuestionTemplateRepositoryPostgres()


def add_question_template(db, args):
    # if (args.type not in ["multiple choice", "written", "media"]):
    #    raise InvalidQuestionTypeException()
    new_question_template = QuestionTemplate(
        id=uuid4(),
        exam_id=args.exam_id,
        question=args.question,
        # type = args.type,#QuestionTypeEnum.multiple_choice,
    )
    # if(args.type == "written"):
    #    new_question_template.type = QuestionTypeEnum.written
    # if(args.type == "media"):
    #    new_question_template.type = QuestionTypeEnum.media

    if args.is_written != None:
        new_question_template.is_written = args.is_written
    if args.is_media != None:
        new_question_template.is_media = args.is_media
    if args.is_written != None:
        new_question_template.options = args.options
    if args.is_written != None:
        new_question_template.correct = args.correct
    if args.is_written != None:
        new_question_template.value = args.value

    qtrp.add_question_template(db, new_question_template)
    return QuestionTemplateSerializer.serialize(new_question_template)
