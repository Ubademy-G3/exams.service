from abc import ABC, abstractmethod


class QuestionTemplateRepository(ABC):

    @abstractmethod
    def add_question_template(self, payload):
        pass

    @abstractmethod
    def get_question_templates(self, exam_id):
        pass

    @abstractmethod
    def delete_question_templates(self, exam_id):
        pass
