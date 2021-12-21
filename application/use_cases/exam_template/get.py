from persistence.repositories.exam_template_repository_postgres import ExamTemplateRepositoryPostgres
from exceptions.http_exception import NotFoundException
from application.serializers.exam_template_serializer import ExamTemplateSerializer
import logging

logger = logging.getLogger(__name__)

etrp = ExamTemplateRepositoryPostgres()


def get_exam_template(db, exam_template_id):
    exam_template = etrp.get_exam_template(db, exam_template_id)
    if exam_template is None:
        logger.warning("Exam template %s not found", exam_template_id)
        raise NotFoundException("Exam template {}".format(exam_template_id))
    return ExamTemplateSerializer.serialize(exam_template)


def get_all_exam_templates_by_course_id(db, course_id, has_multiple_choice, has_written, has_media, state):
    exam_templates = etrp.get_all_exam_templates_by_course_id(db, course_id, has_multiple_choice,
                                                              has_written, has_media, state)

    exam_template_list = []
    for exam_template in exam_templates:
        exam_template_list.append(ExamTemplateSerializer.serialize(exam_template))
    return {
        "course_id": course_id,
        "amount": len(exam_template_list),
        "exam_templates": exam_template_list,
    }


def get_all_exam_templates_by_creator_id(db, creator_id, has_multiple_choice, has_written, has_media, state):
    exam_templates = etrp.get_all_exam_templates_by_creator_id(db, creator_id, has_multiple_choice,
                                                               has_written, has_media, state)

    exam_template_list = []
    for exam_template in exam_templates:
        exam_template_list.append(ExamTemplateSerializer.serialize(exam_template))
    return {
        "creator_id": creator_id,
        "amount": len(exam_template_list),
        "exam_templates": exam_template_list,
    }


def exam_template_exists(db, exam_template_id):
    return etrp.get_exam_template(db, exam_template_id)
