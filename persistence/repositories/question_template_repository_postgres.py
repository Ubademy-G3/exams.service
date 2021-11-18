from infrastructure.db.exam_solution_schema import ExamSolution
from sqlalchemy import func

class QuestionTemplateRepositoryPostgres():

    def add_question_template(self, question_template):
        db.add(question_template)
        db.commit()

    #revisar este que onda
    def get_question_template(self, question_template_id):
        question_templates = db.query(QuestionTemplate).filter(QuestionTemplate.id == question_template_id)
        return question_templates

    def get_question_templates_by_exam_id(self, exam_template_id):
        query = db.query(QuestionTemplate).filter(QuestionTemplate.exam_id == exam_template_id)
        question_templates = query.all()
        return question_templates

    def delete_question_template(self, question_template):
        db.delete(question_template)
        db.commit()
    '''
    def delete_question_templates(self, question_templates):
        db.delete(question_templates)
        db.commit()
    '''
    def update_question_template(self, db):
        db.commit()