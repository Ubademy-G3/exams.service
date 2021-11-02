from domain.exam_template_model import ExamTemplate
from infrastructure.db.database import database
from infrastructure.db.exam_template_schema import exam_templates
from domain.exam_template_repository import ExamTemplateRepository
from uuid import uuid4, UUID


class ExamTemplateRepositoryPostgres(ExamTemplateRepository):

    async def add_exam_template(self, exam_template: ExamTemplate):
        query = exam_templates.insert().values(**exam_template.dict())
        return await database.execute(query=query)

    async def get_all_exams(self):
        query = exam_templates.select()
        return await database.fetch_all(query=query)

    async def get_exam_by_id(self, id: UUID):
        query = exam_templates.select(exam_templates.c.id == id)
        return await database.fetch_one(query=query)

    async def update_exam(self, id: UUID, payload: ExamTemplate):
        query = (exam_templates.update().
                 where(exam_templates.c.id == id)
                 .values(**payload.dict()))
        return await database.execute(query=query)

    async def delete_exam(self, id: UUID):
        query = exam_templates.delete().where(exam_templates.c.id == id)
        return await database.execute(query=query)

    async def delete_all_exams(self):
        query = exam_templates.delete()
        return await database.execute(query=query)
