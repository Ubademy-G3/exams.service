from infrastructure.db.database import Base
from sqlalchemy import (Column, Integer, String, Table, MetaData, ForeignKey, JSON)
from sqlalchemy.dialects.postgresql import (UUID, ARRAY)
import uuid

class QuestionSolution(Base):
    __tablename__ = "question_solutions"
    id = Column(UUID, primary_key=True, nullable = False)
    exam_solution_id = Column(UUID, ForeignKey('exam_solutions.id'), nullable = False)
    question_template_id = Column(UUID, ForeignKey('question_templates.id'), nullable = False)
    answer = Column(String(300), nullable = False)
    score = Column(Integer)

    def __init__(self, id, exam_solution_id, question_template_id, answer, score):
        self.id = id
        self.exam_solution_id = exam_solution_id
        self.question_template_id = question_template_id
        self.answer = answer
        self.score = score
