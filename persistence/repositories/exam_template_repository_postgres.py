from domain.exam_template_model import (ExamTemplate, ExamTemplatePatch)
from infrastructure.db.database import database
from infrastructure.db.exam_template_schema import exam_templates
from domain.exam_template_repository import ExamTemplateRepository

class ExamTemplateRepositoryPostgres(ExamTemplateRepository):

    async def add_exam_template(self, exam_template: ExamTemplate):
        query = exam_templates.insert().values(**exam_template.dict())
        return await database.execute(query=query)

    async def get_exam_template(self, id: str):
        query = exam_templates.select(exam_templates.c.id == id)
        return await database.fetch_one(query=query)

    async def get_all_exam_templates(self):
        query = exam_templates.select()
        return await database.fetch_all(query=query)

    async def delete_exam_template(self, id: str):
        query = exam_templates.delete().where(exam_templates.c.id == id)
        return await database.execute(query=query)

    async def update_exam_template(self, id: str, payload: ExamTemplatePatch):
        query = (exam_templates.update().
                where(exam_templates.c.id == id)
                .values(**payload.dict()))
        return await database.execute(query=query)