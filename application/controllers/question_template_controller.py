from domain.question_template_model import (QuestionTemplate, QuestionTemplatePatch)
from application.use_cases.question_template import *

class QuestionTemplateController:
    @classmethod
    async def create_question_template(self, args):
        return await add_question_template(new_question_template)

    @classmethod
    async def delete_question_template(self, question_template_id):
        return await delete_question_template(question_template_id)