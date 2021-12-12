from persistence.repositories.exam_template_repository_postgres import ExamTemplateRepositoryPostgres
from exceptions.http_exception import NotFoundException
import logging

logger = logging.getLogger(__name__)

etrp = ExamTemplateRepositoryPostgres()


def delete_exam_template(db, exam_template_id):
    exam_template = etrp.get_exam_template(db, exam_template_id)
    if not exam_template:
        logger.warning("Exam template %s not found", exam_template_id)
        raise NotFoundException("Exam template {}".format(exam_template_id))
    return etrp.delete_exam_template(db, exam_template)
