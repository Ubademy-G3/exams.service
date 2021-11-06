from persistence.repositories.exam_solution_repository_postgres import ExamSolutionRepositoryPostgres

etrp = ExamSolutionRepositoryPostgres()

async def add_exam_solution(args):
    new_exam_solution = ExamSolution(
        id = args.id,
        name = args.name,
        course_id = args.course_id,
        user_id = args.user_id,
        answers = args.anwers,
        graded = args.graded,
        score = args.score,
        aprobal_state = args.aprobal_state
    )
    await etrp.add_exam_solution(exam_solution)
    return {
        "id": args.id,
        "name": args.name,
        "course_id": args.course_id,
        "user_id": args.user_id,
        "answers": args.anwers,
        "graded": args.graded,
        "score": args.score,
        "aprobal_state": args.aprobal_state
    }

'''
async def update_exam_solution(id, new_args):
    exam_solution_to_update = await get_exam_solution(exam_solution_id)
    if not exam_solution_to_update:
        raise HTTPException(status_code=404, detail="Exam solution {exam_solution_id} not found")

    exam_solution_in_db = ExamSolution(**exam_solution_to_update)
    if update_args.name is not None:
        exam_solution_in_db.name = update_args.name

    if update_args.questions is not None:
        exam_solution_in_db.questions = update_args.questions

    update_data = exam_solution_in_db.dict(exclude_unset = True)
    update_exam_solution = exam_solution_in_db.copy(update = update_data)
    
    result = await etrp.update_exam_solution(id, new_args)
    return result
'''