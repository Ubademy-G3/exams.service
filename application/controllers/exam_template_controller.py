from application.use_cases.exam_template import create, get, delete, update


class ExamTemplateController:
    @classmethod
    def create_exam_template(self, db, args):
        return create.add_exam_template(db, args)

    @classmethod
    def get_exam_template(self, db, exam_template_id):
        return get.get_exam_template(db, exam_template_id)

    @classmethod
    def get_all_exam_templates_by_course_id(self, db, course_id, has_multiple_choice, has_written, has_media, state):
        return get.get_all_exam_templates_by_course_id(db, course_id, has_multiple_choice, has_written, has_media, state)

    @classmethod
    def get_all_exam_templates_by_creator_id(self, db, creator_id, has_multiple_choice, has_written, has_media, state):
        return get.get_all_exam_templates_by_creator_id(db, creator_id, has_multiple_choice, has_written, has_media, state)

    @classmethod
    def delete_exam_template(self, db, exam_template_id):
        return delete.delete_exam_template(db, exam_template_id)

    @classmethod
    def update_exam_template(self, db, exam_template_id, payload):
        return update.update_exam_template(db, exam_template_id, payload)
