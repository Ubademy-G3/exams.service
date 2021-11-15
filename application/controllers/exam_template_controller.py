from domain.exam_template_model import *
from application.use_cases.exam_template.add_exam_template import add_exam_template
from application.use_cases.exam_template.update_exam_template import update_exam_template
from application.use_cases.exam_template.get_exam_template import get_exam_template
from application.use_cases.exam_template.delete_exam_template import delete_exam_template

class ExamTemplateController:
    @classmethod
    async def create_exam_template(self, args):
        return await add_exam_template(args)

    @classmethod
    async def get_exam_template(self, exam_template_id):
        return await get_exam_template(exam_template_id)
    
    @classmethod
    async def delete_exam_template(self, exam_template_id):
        return await delete_exam_template(exam_template_id)
    
    @classmethod
    async def update_exam_template(self, exam_template_id, payload):
        return await update_exam_template(exam_template_id, payload)
    