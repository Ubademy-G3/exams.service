from persistence.repositories.exam_template_repository_postgres import ExamTemplateRepositoryPostgres
from application.serializers.exam_template_serializer import ExamTemplateSerializer
from domain.exam_template_model import (ExamTemplate, ExamStateEnum)
from exeptions.ubademy_exeption import InvalidExamStateException
etrp = ExamTemplateRepositoryPostgres()
from uuid import uuid4

async def add_exam_template(args):
    #if(args.state not in ["draft", "active"]):
    #    raise InvalidExamStateException()
    new_exam_template = ExamTemplate(
        id = uuid4(),
        name = args.name,
        course_id = args.course_id,
        state = args.state#ExamStateEnum.draft
    )
    #if(args.state == "active"):
    #    new_exam_template.state = ExamStateEnum.active
    await etrp.add_exam_template(new_exam_template)
    return ExamTemplateSerializer.serialize(new_exam_template)