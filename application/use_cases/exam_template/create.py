from persistence.repositories.exam_template_repository_postgres import ExamTemplateRepositoryPostgres
from application.serializers.exam_template_serializer import ExamTemplateSerializer
from infrastructure.db.exam_template_schema import ExamTemplate, ExamStateEnum
from uuid import uuid4
from exceptions.ubademy_exception import InvalidExamStateException


etrp = ExamTemplateRepositoryPostgres()


def add_exam_template(db, args):

    new_exam_template = ExamTemplate(
        id=uuid4(),
        name=args.name,
        course_id=args.course_id,
        state=ExamStateEnum.draft,
        max_score=10,
        has_multiple_choice=False,
        has_written=False,
        has_media=False,
    )

    etrp.add_exam_template(db, new_exam_template)
    return ExamTemplateSerializer.serialize(new_exam_template)
