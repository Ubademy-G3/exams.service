from domain.question_template_model import *
from application.use_cases.question_template.add_question_template import add_question_template
from application.use_cases.question_template.get_question_templates import get_question_templates
from application.use_cases.question_template.delete_question_templates import delete_question_templates

class QuestionTemplateController:
    @classmethod
    async def create_question_template(self, args):
        return await add_question_template(args)

    @classmethod
    async def get_question_templates(self, question_template_id):
        return await get_question_templates(question_template_id)

    @classmethod
    async def delete_question_templates(self, question_template_id):
        return await delete_question_templates(question_template_id)