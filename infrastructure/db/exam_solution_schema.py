from infrastructure.db.database import Base
from sqlalchemy import (Column, Integer, String, Table, MetaData, ForeignKey, Boolean)
from sqlalchemy.dialects.postgresql import (UUID, ARRAY)
import uuid

class ExamSolution(Base):
    __tablename__ = "exam_solutions"
    id = Column(UUID, primary_key = True, nullable = False)
    course_id = Column(UUID, nullable = False)
    user_id = Column(UUID, nullable = False)
    exam_template_id = Column(UUID, nullable = False)
    graded = Column(Boolean)
    score = Column(Integer)
    aprobal_state = Column(Boolean)

    def __init__(self, id, course_id, user_id, exam_template_id, graded, score, aprobal_state):
        self.id = id
        self.course_id = course_id
        self.user_id = user_id
        self.exam_template_id = exam_template_id
        self.graded = graded
        self.score = score
        self.aprobal_state = aprobal_state
