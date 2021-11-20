from infrastructure.db.question_template_schema import QuestionTemplate


class QuestionTemplateSerializer:
    @classmethod
    def serialize(self, question_template: QuestionTemplate):
        return {
            "id": question_template.id,
            "exam_id": question_template.exam_id,
            "question": question_template.question,
            "is_written": question_template.is_written,
            "is_media": question_template.is_media,
            "options": question_template.options,
            "correct": question_template.correct,
            "value": question_template.value,
        }
