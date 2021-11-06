from persistence.repositories.exam_template_repository_postgres import ExamTemplateRepositoryPostgres
from application.serializers.exam_solution_serializer import ExamSolutionSerializer

etrp = ExamTemplateRepositoryPostgres()

async def add_exam_template(args):
    new_exam_template = ExamTemplate(
        id = args.id,
        name = args.name,
        course_id = args.course_id,
        questions = args.questions
    )
    await etrp.add_exam_template(exam_template)
    return ExamTemplateSerializer.serialize(new_exam_template)