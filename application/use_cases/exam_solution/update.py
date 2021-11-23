from persistence.repositories.exam_solution_repository_postgres import ExamSolutionRepositoryPostgres
from exceptions.http_exception import NotFoundException
from application.serializers.exam_solution_serializer import ExamSolutionSerializer
from exceptions.ubademy_exception import NonPositiveExamSolutionScoreException


esrp = ExamSolutionRepositoryPostgres()


def update_exam_solution(db, exam_solution_id, new_args):

    if new_args.score is not None and new_args.score <= 0:
        raise NonPositiveExamSolutionScoreException(new_args.score)

    exam_solution_to_update = esrp.get_exam_solution(db, exam_solution_id)
    if not exam_solution_to_update:
        raise NotFoundException("Exam solution {}".format(exam_solution_id))

    exam_solution_to_update.corrector_id = new_args.corrector_id
    exam_solution_to_update.graded = new_args.graded
    exam_solution_to_update.score = new_args.score
    exam_solution_to_update.approval_state = new_args.approval_state

    esrp.update_exam_solution(db)
    return ExamSolutionSerializer.serialize(exam_solution_to_update)
