from abc import ABC, abstractmethod


class QuestionTemplateRepository(ABC):

    @abstractmethod
    def add_question_template(self, payload):
        pass

    @abstractmethod
    def get_all_question_templates(self):
        pass

    @abstractmethod
    def get_question_template(self, id):
        pass

    @abstractmethod
    def update_question_template(self, id, payload):
        pass

    @abstractmethod
    def delete_question_template(self, id):
        pass

    @abstractmethod
    def delete_all_question_templates(self):
        pass
