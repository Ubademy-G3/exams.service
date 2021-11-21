from infrastructure.db.exam_template_schema import ExamTemplate


class ExamTemplateRepositoryPostgres:
    def add_exam_template(self, db, exam_template):
        db.add(exam_template)
        db.commit()

    def get_exam_template(self, db, exam_template_id):
        exam_template = db.query(ExamTemplate).filter(ExamTemplate.id == exam_template_id).first()
        return exam_template

    def get_all_exam_templates_by_course_id(self, db, course_id, has_multiple_choice, has_written, has_media, state):
        query = db.query(ExamTemplate).filter(ExamTemplate.course_id == course_id)
        if has_multiple_choice is not None:
            query = query.filter(ExamTemplate.has_multiple_choice == has_multiple_choice)
        if has_written is not None:
            query = query.filter(ExamTemplate.has_written == has_written)
        if has_media is not None:
            query = query.filter(ExamTemplate.has_media == has_media)
        if state is not None:
            query = query.filter(ExamTemplate.state == state)
        exam_templates = query.all()
        return exam_templates

    def delete_exam_template(self, db, exam_template):
        db.delete(exam_template)
        db.commit()

    def update_exam_template(self, db):
        db.commit()
