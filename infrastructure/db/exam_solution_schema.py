from infrastructure.db.database import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, ForeignKey, Boolean
from sqlalchemy.dialects.postgresql import UUID
import uuid


class ExamSolution(Base):
    __tablename__ = "exam_solutions"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4())
    course_id = Column(UUID(as_uuid=True), nullable=False)
    user_id = Column(UUID(as_uuid=True), nullable=False)
    exam_template_id = Column(UUID(as_uuid=True), ForeignKey("exam_templates.id", ondelete="CASCADE"), nullable=False)
    graded = Column(Boolean)
    score = Column(Integer)
    aprobal_state = Column(Boolean)

    # Relationships
    question_solution = relationship("QuestionSolution", cascade="all, delete")

    def __init__(self, id, course_id, user_id, exam_template_id, graded, score, aprobal_state):
        self.id = id
        self.course_id = course_id
        self.user_id = user_id
        self.exam_template_id = exam_template_id
        self.graded = graded
        self.score = score
        self.aprobal_state = aprobal_state
