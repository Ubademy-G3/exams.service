from persistence.repositories.question_template_repository_postgres import QuestionTemplateRepositoryPostgres
from application.serializers.question_template_serializer import QuestionTemplateSerializer
from domain.question_template_model import (QuestionTemplate, QuestionTypeEnum)
from exeptions.ubademy_exeption import InvalidQuestionTypeException
from uuid import uuid4

etrp = QuestionTemplateRepositoryPostgres()

async def add_question_template(args):
    #if (args.type not in ["multiple choice", "written", "media"]):
    #    raise InvalidQuestionTypeException()
    new_question_template = QuestionTemplate(
        id = uuid4(),
        exam_id = args.exam_id,
        question = args.question,
        type = args.type,#QuestionTypeEnum.multiple_choice,
        options = args.options,
        correct = args.correct
    )
    #if(args.type == "written"):
    #    new_question_template.type = QuestionTypeEnum.written
    #if(args.type == "media"):
    #    new_question_template.type = QuestionTypeEnum.media
    await etrp.add_question_template(new_question_template)
    return QuestionTemplateSerializer.serialize(new_question_template)
