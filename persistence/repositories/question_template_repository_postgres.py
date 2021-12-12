from infrastructure.db.question_template_schema import QuestionTemplate
import logging

logger = logging.getLogger(__name__)

class QuestionTemplateRepositoryPostgres:
    def add_question_template(self, db, question_template):
        db.add(question_template)
        db.commit()
        logger.info("Added new question template")
        logger.debug("ID of the new question template: %s", question_template.id)

    def get_question_template(self, db, question_template_id):
        question_templates = db.query(QuestionTemplate).filter(QuestionTemplate.id == question_template_id).first()
        logger.debug("Getting question template %s", question_template_id)
        return question_templates

    def get_all_question_templates_by_exam_template_id(self, db, exam_template_id):
        query = db.query(QuestionTemplate).filter(QuestionTemplate.exam_id == exam_template_id)
        question_templates = query.all()
        logger.debug("Getting all question templates of exam template %s", exam_template_id)
        return question_templates

    def delete_question_template(self, db, question_template):
        db.delete(question_template)
        db.commit()
        logger.debug("Delete question template %s", question_template.id)
        logger.info("Question template deleted")

    def update_question_template(self, db):
        db.commit()
