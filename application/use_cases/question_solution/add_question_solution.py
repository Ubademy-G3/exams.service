from persistence.repositories.question_solution_repository_postgres import QuestionSolutionRepositoryPostgres

etrp = QuestionSolutionRepositoryPostgres()

async def add_question_solution(args):
    new_question_solution = QuestionSolution(
        id = args.id,
        exam_id = args.exam_id,
        question = args.question,
        type = args.type,
        options = args.options,
        correct = args.correct,
        user_id = args.user_id,
        answer = args.answer
    )
    await etrp.add_question_solution(question_solution)
    return {
        "id": args.id,
        "exam_id": args.exam_id,
        "question": args.question,
        "type": args.type,
        "options": args.options,
        "correct": args.correct,
        "user_id": args.user_id,
        "answer": args.answer
    }

'''
async def update_question_solution(id, new_args):
    question_solution_to_update = await get_question_solution(question_solution_id)
    if not question_solution_to_update:
        raise HTTPException(status_code=404, detail="Question solution {question_solution_id} not found")

    question_solution_in_db = QuestionSolution(**question_solution_to_update)

    if update_args.correct is not None:
        question_solution_in_db.correct = update_args.correct
        
    update_data = question_solution_in_db.dict(exclude_unset = True)
    update_question_solution = question_solution_in_db.copy(update = update_data)
    
    result = await etrp.update_question_solution(id, new_args)
    return result
'''
