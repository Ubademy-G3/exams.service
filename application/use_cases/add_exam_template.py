from persistence.repositories.exam_template_repository_postgres import ExamTemplateRepositoryPostgres
from persistence.repositories.question_template_repository_postgres import QuestionTemplateRepositoryPostgres
from application.serializers.exam_template_serializer import ExamTemplateSerializer

etrp = ExamTemplateRepositoryPostgres()

async def add_exam_template(args):
    new_exam_template = ExamTemplate(
        name = args.name,
        course_id = args.course_id
    )
    await etrp.add_exam_template(exam_template)
    for i in args.questions:
        new_question_template = QuestionTemplate(
            exam_id = new_exam_template.id,
            question = i.question,
            type = i.type,
            options = i.options,
            correct = i.correct
        )
        await etrp.add_question_template(question_template)
    return ExamTemplateSerializer.serialize(new_exam_template) #revisar