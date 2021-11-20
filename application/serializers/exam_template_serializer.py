from infrastructure.db.exam_template_schema import ExamTemplate


class ExamTemplateSerializer:
    @classmethod
    def serialize(self, exam_template: ExamTemplate):
        return {
            "id": exam_template.id,
            "name": exam_template.name,
            "course_id": exam_template.course_id,
            "state": exam_template.state,
            "max_score": exam_template.max_score,
            "has_multiple_choice": exam_template.has_multiple_choice,
            "has_written": exam_template.has_written,
            "has_media": exam_template.has_media,
        }
