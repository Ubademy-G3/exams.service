from domain.exam_template_model import *
from application.use_cases.add_exam_template import *

class ExamTemplateController:
    @classmethod
    async def create_exam_template(self, args):
        return await add_exam_template(new_exam_template)
'''
    @classmethod
    async def get_exam_template(self, exam_template_id):
        return await get_exam_template(exam_template_id)
    
    @classmethod
    async def delete_exam_template(self, exam_template_id):
        return await delete_exam_template(exam_template_id)
    
    @classmethod
    async def update_exam_template(self, exam_template_id, payload):
        return await update_exam_template(exam_template_id, payload)
'''