from persistence.repositories.exam_template_repository_postgres import ExamTemplateRepositoryPostgres
from application.serializers.exam_template_serializer import ExamTemplateSerializer
from infrastructure.db.exam_template_schema import ExamTemplate  # (ExamTemplate, ExamStateEnum)
from exeptions.ubademy_exeption import InvalidExamStateException

etrp = ExamTemplateRepositoryPostgres()
from uuid import uuid4


def add_exam_template(db, args):
    # if(args.state not in ["draft", "active"]):
    #    raise InvalidExamStateException()
    new_exam_template = ExamTemplate(
        id=uuid4(),
        name=args.name,
        course_id=args.course_id,
        # state = args.state#ExamStateEnum.draft
    )

    # if(args.state == "active"):
    #    new_exam_template.state = ExamStateEnum.active
    etrp.add_exam_template(db, new_exam_template)
    return ExamTemplateSerializer.serialize(new_exam_template)
