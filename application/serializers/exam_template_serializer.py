from infrastructure.db.exam_template_schema import ExamTemplate


class ExamTemplateSerializer:
    @classmethod
    def serialize(self, exam_template: ExamTemplate):
        return {
            "id": exam_template.id,
            "name": exam_template.name,
            "course_id": exam_template.course_id,
            "active": exam_template.active,
        }
