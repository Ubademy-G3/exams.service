from persistence.repositories.question_template_repository_postgres import QuestionTemplateRepositoryPostgres
from application.serializers.question_template_serializer import QuestionTemplateSerializer
from infrastructure.db.question_template_schema import QuestionTemplate, QuestionTypeEnum
from exceptions.ubademy_exception import InvalidQuestionTypeException
from uuid import uuid4


from exceptions.ubademy_exception import InvalidQuestionTypeException


qtrp = QuestionTemplateRepositoryPostgres()


def add_question_template(db, exam_template_id, args):
    if (args.question_type is not None and args.question_type not in ["multiple_choice", "written", "media"]):
        raise InvalidQuestionTypeException(new_args.question_type)
    new_question_template = QuestionTemplate(
        id=uuid4(),
        exam_id=exam_template_id,
        question=args.question,
        question_type=QuestionTypeEnum.multiple_choice,
        options=args.options,
        correct=args.correct,
        value=args.value,
    )
    
    if(args.type == "written"):
        new_question_template.question_type = QuestionTypeEnum.written
    if(args.type == "media"):
        new_question_template.question_type = QuestionTypeEnum.media

    if new_question_template.options is None:
        new_question_template.options = {}
    if new_question_template.correct is None:
        new_question_template.correct = 0
    if new_question_template.value is None:
        new_question_template.value = 1

    qtrp.add_question_template(db, new_question_template)
    return QuestionTemplateSerializer.serialize(new_question_template)
