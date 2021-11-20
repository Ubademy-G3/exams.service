from application.use_cases.question_template import create, get, delete, update


class QuestionTemplateController:
    @classmethod
    def create_question_template(self, db, args):
        return create.add_question_template(db, args)

    @classmethod
    def get_question_template(self, db, question_template_id):
        return get.get_question_template(db, question_template_id)

    @classmethod
    def get_all_question_templates_by_exam_template_id(db, exam_template_id):
        return get.get_all_question_templates_by_exam_template_id(db, exam_template_id)

    @classmethod
    def delete_question_templates(self, db, question_template_id):
        return delete.delete_question_templates(db, question_template_id)

    @classmethod
    def update_question_template(self, db, question_template_id, payload):
        return update.update_question_template(db, question_template_id, payload)
