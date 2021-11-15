from abc import ABC, abstractmethod


class QuestionSolutionRepository(ABC):

    @abstractmethod
    def add_question_solution(self, payload):
        pass

    @abstractmethod
    def get_question_solutions(self, id):
        pass

    @abstractmethod
    def delete_question_solutions(self, id):
        pass
