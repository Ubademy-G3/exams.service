from persistence.repositories.question_template_repository_postgres import QuestionTemplateRepositoryPostgres

etrp = QuestionTemplateRepositoryPostgres()

async def update_question_template(id, new_args):
    question_template_to_update = await get_question_template(question_template_id)
    if not question_template_to_update:
        raise HTTPException(status_code=404, detail="Question template {question_template_id} not found")

    question_template_in_db = QuestionTemplate(**question_template_to_update)

    if update_args.question is not None:
        question_template_in_db.question = update_args.question

    if update_args.type is not None:
        question_template_in_db.type = update_args.type

    if update_args.options is not None:
        question_template_in_db.options = update_args.options

    if update_args.correct is not None:
        question_template_in_db.correct = update_args.correct
        
    update_data = question_template_in_db.dict(exclude_unset = True)
    update_question_template = question_template_in_db.copy(update = update_data)
    
    result = await etrp.update_question_template(id, new_args)
    return result
