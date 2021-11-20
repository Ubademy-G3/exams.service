from infrastructure.db.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
import uuid


class QuestionSolution(Base):
    __tablename__ = "question_solutions"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4())
    exam_solution_id = Column(UUID(as_uuid=True), ForeignKey("exam_solutions.id", ondelete="CASCADE"), nullable=False)
    question_template_id = Column(UUID(as_uuid=True), ForeignKey("question_templates.id", ondelete="CASCADE"), nullable=False)
    answer = Column(String(300), nullable=False)
    score = Column(Integer)

    def __init__(self, id, exam_solution_id, question_template_id, answer, score):
        self.id = id
        self.exam_solution_id = exam_solution_id
        self.question_template_id = question_template_id
        self.answer = answer
        self.score = score
