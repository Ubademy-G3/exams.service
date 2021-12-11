from persistence.repositories.exam_template_repository_postgres import ExamTemplateRepositoryPostgres
from application.serializers.exam_template_serializer import ExamTemplateSerializer
from infrastructure.db.exam_template_schema import ExamTemplate, ExamStateEnum
from uuid import uuid4


etrp = ExamTemplateRepositoryPostgres()


def add_exam_template(db, args):

    new_exam_template = ExamTemplate(
        id=uuid4(),
        course_id=args.course_id,
        creator_id=args.creator_id,
        name=args.name,
        state=ExamStateEnum.draft,
        max_score=10,
        approval_score=5,
        has_multiple_choice=False,
        has_written=False,
        has_media=False,
        max_attempts=1,
    )

    etrp.add_exam_template(db, new_exam_template)
    return ExamTemplateSerializer.serialize(new_exam_template)
