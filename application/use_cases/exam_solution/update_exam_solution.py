from persistence.repositories.exam_solution_repository_postgres import ExamSolutionRepositoryPostgres
from domain.exam_solution_model import *
from errors.http_error import NotFoundError
from application.serializers.exam_solution_serializer import ExamSolutionSerializer

etrp = ExamSolutionRepositoryPostgres()

async def update_exam_solution(exam_solution_id, new_args):
    
    exam_solution_to_update = await etrp.get_exam_solution(exam_solution_id)
    if not exam_solution_to_update:
        raise NotFoundError("Exam solution {}".format(exam_solution_id))

    exam_solution_in_db = ExamSolution(**exam_solution_to_update)

    if new_args.graded is not None:
        exam_solution_in_db.graded = new_args.graded
        
    if new_args.score is not None:
        exam_solution_in_db.score = new_args.score
        
    if new_args.aprobal_state is not None:
        exam_solution_in_db.aprobal_state = new_args.aprobal_state
    
    update_data = exam_solution_in_db.dict(exclude_unset=True)
    updated_exam_solution = exam_solution_in_db.copy(update=update_data)
    await etrp.update_exam_solution(exam_solution_id, updated_exam_solution)
    return ExamSolutionSerializer.serialize(updated_exam_solution)