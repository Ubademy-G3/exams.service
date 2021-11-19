from persistence.repositories.question_template_repository_postgres import QuestionTemplateRepositoryPostgres
from exeptions.http_exeption import NotFoundExeption
from application.serializers.question_template_serializer import QuestionTemplateSerializer

qtrp = QuestionTemplateRepositoryPostgres()

def get_question_templates(db, question_template_id):
    question_templates = qtrp.get_question_templates(db, question_template_id)
    if question_templates is None:
        raise NotFoundExeption("Question template {}".format(question_template_id))
    return QuestionTemplateSerializer.serialize(question_template)

def get_all_question_templates_by_exam_template_id(db, exam_template_id):
    question_templates = etrp.get_all_question_templates_by_exam_template_id(db, exam_template_id)
    if question_templates is None or len(question_templates) == 0:
        raise NotFoundExeption("Question templates by exam_template_id {}".format(exam_template_id))
    question_template_list = []
    for question_template in question_templates:
        question_template_list.append(QuestionTemplateSerializer.serialize(question_template))
    return question_template_list

def question_template_exists(db, question_template_id):
    return qtrp.get_question_template(db, question_template_id)