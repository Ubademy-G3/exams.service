from infrastructure.db.exam_template_schema import ExamTemplate
import logging

logger = logging.getLogger(__name__)

class ExamTemplateRepositoryPostgres:
    def add_exam_template(self, db, exam_template):
        db.add(exam_template)
        db.commit()
        logger.info("Added new exam template")
        logger.debug("Name of the new user: %s", exam_template.name)

    def get_exam_template(self, db, exam_template_id):
        exam_template = db.query(ExamTemplate).filter(ExamTemplate.id == exam_template_id).first()
        logger.debug("Getting exam template %s", exam_template_id)
        return exam_template

    def get_all_exam_templates_by_course_id(self, db, course_id, has_multiple_choice, has_written, has_media, state):
        query = db.query(ExamTemplate).filter(ExamTemplate.course_id == course_id)
        if has_multiple_choice is not None:
            logger.debug("Get exam templates of course %s with filter has_multiple_choice", course_id, has_multiple_choice)
            query = query.filter(ExamTemplate.has_multiple_choice == has_multiple_choice)
        if has_written is not None:
            logger.debug("Get exam templates of course %s with filter has_written", course_id, has_written)
            query = query.filter(ExamTemplate.has_written == has_written)
        if has_media is not None:
            logger.debug("Get exam templates of course %s with filter has_media", course_id, has_media)
            query = query.filter(ExamTemplate.has_media == has_media)
        if state is not None:
            logger.debug("Get exam templates of course %s with filter state", course_id, state)
            query = query.filter(ExamTemplate.state == state)
        exam_templates = query.all()
        logger.debug("Getting all exam templates of course %s", course_id)
        return exam_templates

    def get_all_exam_templates_by_creator_id(self, db, creator_id, has_multiple_choice, has_written, has_media, state):
        query = db.query(ExamTemplate).filter(ExamTemplate.creator_id == creator_id)
        if has_multiple_choice is not None:
            logger.debug("Get exam templates of creator %s with filter has_multiple_choice", creator_id, has_multiple_choice)
            query = query.filter(ExamTemplate.has_multiple_choice == has_multiple_choice)
        if has_written is not None:
            logger.debug("Get exam templates of creator %s with filter has_written", creator_id, has_written)
            query = query.filter(ExamTemplate.has_written == has_written)
        if has_media is not None:
            logger.debug("Get exam templates of creator %s with filter has_media", creator_id, has_media)
            query = query.filter(ExamTemplate.has_media == has_media)
        if state is not None:
            logger.debug("Get exam templates of creator %s with filter state", creator_id, state)
            query = query.filter(ExamTemplate.state == state)
        exam_templates = query.all()
        logger.debug("Getting all exam templates of creator %s", creator_id)
        return exam_templates

    def delete_exam_template(self, db, exam_template):
        db.delete(exam_template)
        db.commit()
        logger.debug("Delete exam template %s", exam_template.id)
        logger.info("Exam template deleted")

    def update_exam_template(self, db):
        db.commit()
