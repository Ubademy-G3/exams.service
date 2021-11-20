from persistence.repositories.question_solution_repository_postgres import QuestionSolutionRepositoryPostgres
from exeptions.http_exeption import NotFoundExeption
from application.serializers.question_solution_serializer import QuestionSolutionSerializer

qsrp = QuestionSolutionRepositoryPostgres()

def get_question_solution(db, question_solution_id):
    question_solution = qsrp.get_question_solution(db, question_solution_id)
    if question_solution is None:
        raise NotFoundExeption("Question solution {}".format(question_solution_id))
    return QuestionSolutionSerializer.serialize(question_solution)

def get_all_question_solutions_by_question_template_id(db, question_template_id):
    question_solutions = qsrp.get_all_question_solutions_by_question_template_id(db, question_template_id)
    if question_solutions is None or len(question_solutions) == 0:
        raise NotFoundExeption("Question solutions by question_template_id {}".format(question_template_id))
    question_solution_list = []
    for question_solution in question_solutions:
        question_solution_list.append(QuestionSolutionSerializer.serialize(question_solution))
    return question_solution_list

def get_all_question_solutions_by_exam_solution_id(db, exam_solution_id):
    question_solutions = qsrp.get_all_question_solutions_by_exam_solution_id(db, exam_solution_id)
    if question_solutions is None or len(question_solutions) == 0:
        raise NotFoundExeption("Question solutions by exam_solution_id {}".format(exam_solution_id))
    question_solution_list = []
    for question_solution in question_solutions:
        question_solution_list.append(QuestionSolutionSerializer.serialize(question_solution))
    return question_solution_list