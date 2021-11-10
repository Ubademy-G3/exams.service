from domain.question_template_model import QuestionTemplate
from infrastructure.db.database import database
from infrastructure.db.question_template_schema import question_templates
from domain.question_template_repository import QuestionTemplateRepository

class QuestionTemplateRepositoryPostgres(QuestionTemplateRepository):

    async def add_question_template(self, question_template: QuestionTemplate):
        query = question_templates.insert().values(**question_template.dict())
        return await database.execute(query=query)

    async def get_all_questions(self):
        query = question_templates.select()
        return await database.fetch_all(query=query)

    async def get_question_by_id(self, id: str):
        query = question_templates.select(question_templates.c.id == id)
        return await database.fetch_one(query=query)

    async def delete_question(self, id: str):
        query = question_templates.delete().where(question_templates.c.id == id)
        return await database.execute(query=query)

    async def delete_all_questions(self):
        query = question_templates.delete()
        return await database.execute(query=query)
