from persistence.repositories.exam_template_repository_postgres import ExamTemplateRepositoryPostgres
from exceptions.http_exception import NotFoundException

etrp = ExamTemplateRepositoryPostgres()


def delete_exam_template(db, exam_template_id):
    exam_template = etrp.get_exam_template(db, exam_template_id)
    if not exam_template:
        raise NotFoundException("Exam template {}".format(exam_template_id))
    return etrp.delete_exam_template(db, exam_template_id)
