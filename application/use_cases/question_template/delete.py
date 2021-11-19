from persistence.repositories.question_template_repository_postgres import QuestionTemplateRepositoryPostgres
from exeptions.http_exeption import NotFoundExeption

qtrp = QuestionTemplateRepositoryPostgres()

def delete_question_templates(db, question_template_id):
    question_templates = qtrp.get_question_templates(db, question_template_id)
    if not question_templates:
        raise NotFoundExeption("Question template {}".format(question_template_id))
    return qtrp.delete_question_templates(db, question_template_id)