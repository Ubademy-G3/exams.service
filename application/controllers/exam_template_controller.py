from fastapi import HTTPException
from domain.exam_template_model import (ExamTemplate, ExamTemplatePatch)
from application.use_cases.exam_template import *

class ExamTemplateController:
    @classmethod
    async def create_exam_template(self, args):
        return await add_exam_template(new_exam_template)

    @classmethod
    async def get_exam_template(self, exam_template_id):
        return await get_exam_template(exam_template_id)
    
    @classmethod
    async def get_all_exam_templates(self):
        return await get_all_exam_templates()

    @classmethod
    async def update_exam_template(self, exam_template_id, update_args):
        return await update_exam_template(exam_template_id, update_exam_template)

    @classmethod
    async def delete_exam_template(self, exam_template_id):
        return await delete_exam_template(exam_template_id)

    @classmethod
    async def delete_all_exam_templates(self):
        return await delete_all_exam_templates()
            