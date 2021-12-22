from persistence.repositories.question_template_repository_postgres import QuestionTemplateRepositoryPostgres
from exceptions.http_exception import NotFoundException
import logging
from application.use_cases.exam_template import update

logger = logging.getLogger(__name__)

qtrp = QuestionTemplateRepositoryPostgres()


def delete_question_template(db, exam_template_id, question_template_id):
    question_template = qtrp.get_question_template(db, question_template_id)
    if not question_template:
        logger.warning("Question template %s not found", question_template_id)
        raise NotFoundException("Question template {}".format(question_template_id))
    result = qtrp.delete_question_template(db, question_template)
    update.update_flags(db, exam_template_id)
    return result
