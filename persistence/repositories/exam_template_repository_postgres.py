from infrastructure.db.exam_template_schema import ExamTemplate
from sqlalchemy import func

class ExamTemplateRepositoryPostgres():

    def add_exam_template(self, db, exam_template):
        db.add(exam_template)
        db.commit()

    def get_exam_template(self, db, exam_template_id):
        exam_template = db.query(ExamTemplate).filter(ExamTemplate.id == exam_template_id)
        return exam_template

    def get_exam_templates_by_course_id(self, db, course_id):
        query = db.query(ExamTemplate).filter(ExamTemplate.course_id == course_id)
        exam_templates = query.all()
        return exam_templates
    
    def delete_exam_template(self, db, exam_template):
        db.delete(exam_template)
        db.commit()

    def update_exam_template(self, db):
        db.commit()