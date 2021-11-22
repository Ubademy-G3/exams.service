from infrastructure.db.database import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Float, String, Boolean, Enum
from sqlalchemy.dialects.postgresql import UUID
import uuid
from domain.exam_template_model import ExamStateEnum


class ExamTemplate(Base):

    __tablename__ = "exam_templates"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4())
    name = Column(String(50), nullable=False)
    course_id = Column(UUID(as_uuid=True), nullable=False)
    state = Column(Enum(ExamStateEnum))
    max_score = Column(Float, default=10)
    has_multiple_choice = Column(Boolean, default=True)
    has_written = Column(Boolean, default=False)
    has_media = Column(Boolean, default=False)

    # Relationships
    exam_solution = relationship("ExamSolution", cascade="all, delete")
    question_template = relationship("QuestionTemplate", cascade="all, delete")

    def __init__(self, id, name, course_id, state, max_score, has_multiple_choice, has_written, has_media):
        self.id = id
        self.name = name
        self.course_id = course_id
        self.state = state
        self.max_score = max_score
        self.has_multiple_choice = has_multiple_choice
        self.has_written = has_written
        self.has_media = has_media
