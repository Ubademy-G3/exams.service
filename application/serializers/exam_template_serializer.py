from domain.exam_template_model import ExamTemplate

class ExamTemplateSerializer:

    @classmethod
    def serialize(self, exam_template: ExamTemplate):
        return {
        "id": args.id,
        "name": args.name,
        "course_id": args.course_id
    }