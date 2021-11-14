from persistence.repositories.exam_template_repository_postgres import ExamTemplateRepositoryPostgres
from persistence.repositories.question_template_repository_postgres import QuestionTemplateRepositoryPostgres
from application.serializers.exam_template_serializer import ExamTemplateSerializer
from domain.question_template_model import QuestionTemplate
from domain.exam_template_model import ExamTemplate

etrp = ExamTemplateRepositoryPostgres()
qtrp = QuestionTemplateRepositoryPostgres()

async def get_exam_template(exam_template_id):
    exam = await etrp.get_exam_template(exam_template_id)
    questions = await qtrp.get_question_templates(exam_template_id)
    return  exam.dict().update(questions.dict())