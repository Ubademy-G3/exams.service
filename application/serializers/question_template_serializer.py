from infrastructure.db.question_template_schema import QuestionTemplate
from domain.question_template_model import QuestionTypeEnum


class QuestionTemplateSerializer:
    @classmethod
    def serialize(self, question_template: QuestionTemplate):

        question_type="multiple_choice"
        if question_template.question_type==QuestionTypeEnum.written:
            question_type="written"
        if question_template.question_type==QuestionTypeEnum.media:
            question_type="media"
        return {
            "id": question_template.id,
            "exam_id": question_template.exam_id,
            "question": question_template.question,
            "question_type": question_type,
            "options": question_template.options,
            "correct": question_template.correct,
            "value": question_template.value,
        }
