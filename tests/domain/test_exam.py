from domain.exam_model import Exam


class TestExam:
    def test_constructor_creates_instance(self):
        exam = Exam(id=1234, name="Curso01")

        assert exam.name == "Curso01"
        assert exam.id == 1234
