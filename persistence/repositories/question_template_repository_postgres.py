from infrastructure.db.question_template_schema import QuestionTemplate


class QuestionTemplateRepositoryPostgres:
    def add_question_template(self, db, question_template):
        db.add(question_template)
        db.commit()

    def get_question_template(self, db, question_template_id):
        question_templates = db.query(QuestionTemplate).filter(QuestionTemplate.id == question_template_id).first()
        return question_templates

    def get_all_question_templates_by_exam_template_id(self, db, exam_template_id):
        query = db.query(QuestionTemplate).filter(QuestionTemplate.exam_id == exam_template_id)
        question_templates = query.all()
        return question_templates

    def delete_question_template(self, db, question_template):
        db.delete(question_template)
        db.commit()

    def update_question_template(self, db):
        db.commit()
