from persistence.repositories.question_template_repository_postgres import QuestionTemplateRepositoryPostgres
from exceptions.http_exception import NotFoundException

qtrp = QuestionTemplateRepositoryPostgres()


def delete_question_templates(db, question_template_id):
    question_templates = qtrp.get_question_templates(db, question_template_id)
    if not question_templates:
        raise NotFoundException("Question template {}".format(question_template_id))
    return qtrp.delete_question_templates(db, question_template_id)
