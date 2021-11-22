from infrastructure.db.database import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, Float, String, ForeignKey, JSON, Enum
from sqlalchemy.dialects.postgresql import UUID, ARRAY
import uuid
from domain.question_template_model import QuestionTypeEnum


class QuestionTemplate(Base):
    __tablename__ = "question_templates"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4())
    exam_id = Column(UUID(as_uuid=True), ForeignKey("exam_templates.id", ondelete="CASCADE"), nullable=False)
    question = Column(String(300), nullable=False)
    question_type = Column(Enum(QuestionTypeEnum))
    options = Column(ARRAY(String(300)), default={})
    correct = Column(Integer, default=0)
    value = Column(Float, default=1)

    # Relationships
    question_solution = relationship("QuestionSolution", cascade="all, delete")

    def __init__(self, id, exam_id, question, question_type, options, correct, value):
        self.id = id
        self.exam_id = exam_id
        self.question = question
        self.question_type = question_type
        self.options = options
        self.correct = correct
        self.value = value
