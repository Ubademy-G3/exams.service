from application.use_cases.question_template import (create, get, delete)#, update)

class QuestionTemplateController:
    @classmethod
    def create_question_template(self, db, args):
        return add_question_template(args)

    @classmethod
    def get_question_templates(self, db, question_template_id):
        return get_question_templates(question_template_id)

    @classmethod
    def delete_question_templates(self, db, question_template_id):
        return delete_question_templates(question_template_id)