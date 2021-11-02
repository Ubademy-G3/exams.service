from persistence.repositories.exam_template_repository_postgres import ExamTemplateRepositoryPostgres

etrp = ExamTemplateRepositoryPostgres()

async def update_exam_template(id, new_args):
    exam_template_to_update = await get_exam_template(exam_template_id)
    if not exam_template_to_update:
        raise HTTPException(status_code=404, detail="Exam template {exam_template_id} not found")

    exam_template_in_db = ExamTemplate(**exam_template_to_update)
    if update_args.name is not None:
        exam_template_in_db.name = update_args.name

    if update_args.questions is not None:
        exam_template_in_db.questions = update_args.questions

    update_data = exam_template_in_db.dict(exclude_unset = True)
    update_exam_template = exam_template_in_db.copy(update = update_data)
    
    result = await etrp.update_exam_template(id, new_args)
    return result
