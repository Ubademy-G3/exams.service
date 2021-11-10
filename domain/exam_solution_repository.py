from abc import ABC, abstractmethod


class ExamSolutionRepository(ABC):

    @abstractmethod
    def add_exam_solution(self, payload):
        pass

    @abstractmethod
    def get_all_exam_solutions(self):
        pass

    @abstractmethod
    def get_exam_solution(self, id):
        pass
    
    @abstractmethod
    def delete_exam_solution(self, id):
        pass

    @abstractmethod
    def delete_all_exam_solutions(self):
        pass
