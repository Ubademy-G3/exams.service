from persistence.repositories.question_template_repository_postgres import QuestionTemplateRepositoryPostgres

etrp = QuestionTemplateRepositoryPostgres()

async def add_question_template(args):
    new_question_template = QuestionTemplate(
        id = args.id,
        exam_id = args.exam_id,
        question = args.question,
        type = args.type,
        options = args.options,
        correct = args.correct
    )
    await etrp.add_question_template(question_template)
    return {
        "id": args.id,
        "exam_id": args.exam_id,
        "question": args.question,
        "type": args.type,
        "options": args.options,
        "correct": args.correct
    }
