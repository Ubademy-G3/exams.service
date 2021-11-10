from abc import ABC, abstractmethod


class ExamTemplateRepository(ABC):

    @abstractmethod
    def add_exam_template(self, payload):
        pass

    @abstractmethod
    def get_exam_template(self, id):
        pass

    @abstractmethod
    def delete_exam_template(self, id):
        pass
