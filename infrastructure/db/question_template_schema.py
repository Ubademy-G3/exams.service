from infrastructure.db.database import Base, relationship
from sqlalchemy import (Column, Integer, String, Table, MetaData, ForeignKey, JSON, Boolean)
from sqlalchemy.dialects.postgresql import (UUID, ARRAY)
import uuid
#from domain.question_template_model import QuestionTypeEnum
#from enum import Enum

class QuestionTemplate(Base):
    __tablename__ = "question_templates"
    id = Column(UUID(as_uuid=True), primary_key=True, default = uuid.uuid4())
    exam_id = Column(UUID(as_uuid=True), ForeignKey('exam_templates.id', ondelete="CASCADE"), nullable = False)
    question = Column(String(300), nullable = False)
    is_written = Column(Boolean, default = False)
    is_media = Column(Boolean, default = False)
    options = Column(JSON)
    correct = Column(Integer)
    value = Column(Integer, default = 1)

    #Relationships
    question_solution = relationship("QuestionSolution", cascade = "all, delete")

    def __init__(self, id, exam_id, question, is_written, is_media, options, correct, value):
        self.id = id
        self.exam_id = exam_id
        self.question = question
        self.is_written = is_written
        self.is_media = is_media
        self.options = options
        self.correct = correct
        self.value = value
