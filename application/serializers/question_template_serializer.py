
from domain.question_template_model import QuestionTemplate

class QuestionTemplateSerializer:

    @classmethod
    def serialize(self, question_template: QuestionTemplate):
        return {
        "id": args.id,
        "exam_id": args.exam_id,
        "question": args.question,
        "type": args.type,
        "options": args.options,
        "correct": args.correct
    }