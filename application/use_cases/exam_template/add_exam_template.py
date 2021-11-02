from persistence.repositories.exam_template_repository_postgres import ExamTemplateRepositoryPostgres

etrp = ExamTemplateRepositoryPostgres()

async def add_exam_template(args):
    new_exam_template = ExamTemplate(
        id = args.id,
        name = args.name,
        course_id = args.course_id,
        questions = args.questions
    )
    await etrp.add_exam_template(exam_template)
    return {
        "id": args.id,
        "name": args.name,
        "course_id": args.course_id,
        "questions": args.questions
    }