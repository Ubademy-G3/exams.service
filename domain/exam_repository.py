from abc import ABC, abstractmethod


class ExamRepository(ABC):

    @abstractmethod
    def add_exam(self, payload):
        pass

    @abstractmethod
    def get_all_exams(self):
        pass

    @abstractmethod
    def get_exam_by_id(self, id):
        pass

    @abstractmethod
    def update_exam(self, id, payload):
        pass

    @abstractmethod
    def delete_exam(self, id):
        pass

    @abstractmethod
    def delete_all_exams(self):
        pass
