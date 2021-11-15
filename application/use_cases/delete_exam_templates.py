from persistence.repositories.exam_template_repository_postgres import ExamTemplateRepositoryPostgres
from persistence.repositories.question_template_repository_postgres import QuestionTemplateRepositoryPostgres
from application.serializers.exam_template_serializer import ExamTemplateSerializer
from domain.question_template_model import QuestionTemplate
from domain.exam_template_model import ExamTemplate

etrp = ExamTemplateRepositoryPostgres()
qtrp = QuestionTemplateRepositoryPostgres()

async def delete_exam_template(exam_template_id):
    exam = await etrp.delete_exam_template(exam_template_id)
    questions = await qtrp.delete_question_templates(exam_template_id)
    return  exam #+ questions