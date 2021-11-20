from persistence.repositories.exam_template_repository_postgres import ExamTemplateRepositoryPostgres
from exeptions.http_exeption import NotFoundExeption
from application.serializers.exam_template_serializer import ExamTemplateSerializer

etrp = ExamTemplateRepositoryPostgres()


def get_exam_template(db, exam_template_id):
    exam_template = etrp.get_exam_template(db, exam_template_id)
    if exam_template is None:
        raise NotFoundExeption("Exam template {}".format(exam_template_id))
    return ExamTemplateSerializer.serialize(exam_template)


def get_all_exam_templates_by_course_id(db, course_id, has_multiple_choice, has_written, has_media):
    exam_templates = etrp.get_all_exam_templates_by_course_id(db, course_id, has_multiple_choice, has_written, has_media)
    if exam_templates is None or len(exam_templates) == 0:
        raise NotFoundExeption("Exam templates by course_id {}".format(course_id))
    exam_template_list = []
    for exam_template in exam_templates:
        exam_template_list.append(ExamTemplateSerializer.serialize(exam_template))
    return exam_template_list


def exam_template_exists(db, exam_template_id):
    return etrp.get_exam_template(db, exam_template_id)
