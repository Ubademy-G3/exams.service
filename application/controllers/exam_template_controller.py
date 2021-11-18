from application.use_cases.exam_template import (create, get, delete, update)

class ExamTemplateController:
    @classmethod
    def create_exam_template(self, db, args):
        return add_exam_template(args)

    @classmethod
    def get_exam_template(self, db, exam_template_id):
        return get_exam_template(exam_template_id)
    
    @classmethod
    def delete_exam_template(self, db, exam_template_id):
        return delete_exam_template(exam_template_id)
    
    @classmethod
    def update_exam_template(self, db, exam_template_id, payload):
        return update_exam_template(exam_template_id, payload)
    