from abc import ABC, abstractmethod


class ExamTemplateRepository(ABC):

    @abstractmethod
    def add_exam_template(self, payload):
        pass

    @abstractmethod
    def get_all_exam_templates(self):
        pass

    @abstractmethod
    def get_exam_template(self, id):
        pass

    @abstractmethod
    def update_exam_template(self, id, payload):
        pass

    @abstractmethod
    def delete_exam_template(self, id):
        pass

    @abstractmethod
    def delete_all_exam_templates(self):
        pass
