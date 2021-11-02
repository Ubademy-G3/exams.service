from fastapi import HTTPException
from domain.question_template_model import QuestionTemplate
from application.use_cases.question_template import *

class QuestionTemplateController:
    @classmethod
    async def create_question_template(self, args):
        return await add_question_template(new_question_template)
    
    @classmethod
    async def get_all_question_templates(self):
        return await get_all_question_templates()

    @classmethod
    async def update_question_template(self, question_template_id, update_args):
        return await update_question_template(question_template_id, update_question_template)

    @classmethod
    async def delete_question_template(self, question_template_id):
        return await delete_question_template(question_template_id)

    @classmethod
    async def delete_all_question_templates(self):
        return await delete_all_question_templates()
            