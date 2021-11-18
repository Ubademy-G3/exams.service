from persistence.repositories.question_template_repository_postgres import QuestionTemplateRepositoryPostgres
from exeptions.http_exeption import NotFoundExeption

etrp = QuestionTemplateRepositoryPostgres()

def delete_question_templates(db, question_template_id):
    question_templates = etrp.get_question_templates(db, question_template_id)
    if not question_templates:
        raise NotFoundExeption("Question template {}".format(question_template_id))
    return etrp.delete_question_templates(db, question_template_id)