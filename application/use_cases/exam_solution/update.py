from persistence.repositories.exam_solution_repository_postgres import ExamSolutionRepositoryPostgres
from exeptions.http_exeption import NotFoundExeption
from application.serializers.exam_solution_serializer import ExamSolutionSerializer

esrp = ExamSolutionRepositoryPostgres()

def update_exam_solution(db, exam_solution_id, new_args):
    
    exam_solution_to_update = esrp.get_exam_solution(db, exam_solution_id)
    if not exam_solution_to_update:
        raise NotFoundExeption("Exam solution {}".format(exam_solution_id))

    if new_args.graded is not None:
        exam_solution_to_update.graded = new_args.graded
        
    if new_args.score is not None:
        exam_solution_to_update.score = new_args.score
        
    if new_args.aprobal_state is not None:
        exam_solution_to_update.aprobal_state = new_args.aprobal_state
    
    esrp.update_exam_solution(db)
    return ExamSolutionSerializer.serialize(updated_exam_solution)