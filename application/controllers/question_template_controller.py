from domain.question_template_model import *
from application.use_cases.question_template import *

class QuestionTemplateController:
    @classmethod
    async def create_question_template(self, args):
        return await add_question_template(new_question_template)

    @classmethod
    async def get_question_template(self, question_template_id):
        return await get_question_template(question_template_id)

    @classmethod
    async def delete_question_template(self, question_template_id):
        return await delete_question_template(question_template_id)