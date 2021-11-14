
from domain.question_template_model import QuestionTemplate

class QuestionTemplateSerializer:

    @classmethod
    def serialize(self, question_template: QuestionTemplate):
        return {
        "id": question_template.id,
        "exam_id": question_template.exam_id,
        "question": question_template.question,
        "type": question_template.type,
        "options": question_template.options,
        "correct": question_template.correct
    }