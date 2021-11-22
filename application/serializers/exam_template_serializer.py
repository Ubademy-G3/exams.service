from infrastructure.db.exam_template_schema import ExamTemplate
from domain.exam_template_model import ExamStateEnum


class ExamTemplateSerializer:
    @classmethod
    def serialize(self, exam_template: ExamTemplate):

        state = "draft"
        if exam_template.state == ExamStateEnum.active:
            state = "active"
        if exam_template.state == ExamStateEnum.inactive:
            state = "inactive"
        return {
            "id": exam_template.id,
            "course_id": exam_template.course_id,
            "creator_id": exam_template.creator_id,
            "name": exam_template.name,
            "state": state,
            "max_score": exam_template.max_score,
            "has_multiple_choice": exam_template.has_multiple_choice,
            "has_written": exam_template.has_written,
            "has_media": exam_template.has_media,
        }
