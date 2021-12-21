from persistence.repositories.question_template_repository_postgres import QuestionTemplateRepositoryPostgres
from exceptions.http_exception import NotFoundException
from application.serializers.question_template_serializer import QuestionTemplateSerializer
import logging

logger = logging.getLogger(__name__)

qtrp = QuestionTemplateRepositoryPostgres()


def get_question_template(db, question_template_id):
    question_template = qtrp.get_question_template(db, question_template_id)
    if question_template is None:
        logger.warning("Question template %s not found", question_template_id)
        raise NotFoundException("Question template {}".format(question_template_id))
    return QuestionTemplateSerializer.serialize(question_template)


def get_all_question_templates_by_exam_template_id(db, exam_template_id):
    question_templates = qtrp.get_all_question_templates_by_exam_template_id(db, exam_template_id)
    question_template_list = []
    for question_template in question_templates:
        question_template_list.append(QuestionTemplateSerializer.serialize(question_template))
    return {
        "exam_template_id": exam_template_id,
        "amount": len(question_template_list),
        "question_templates": question_template_list,
    }


def question_template_exists(db, question_template_id):
    return qtrp.get_question_template(db, question_template_id)
