from infrastructure.db.database import Base
from sqlalchemy import (Column, Integer, String, Table, MetaData, ForeignKey, JSON, Boolean)
from sqlalchemy.dialects.postgresql import (UUID, ARRAY)
import uuid
#from domain.question_template_model import QuestionTypeEnum
#from enum import Enum

class QuestionTemplate(Base):
    __tablename__ = "question_templates"
    id = Column(UUID, primary_key=True, nullable = False)
    exam_id = Column(UUID, ForeignKey('exam_templates.id'), nullable = False)
    question = Column(String(300), nullable = False)
    is_written = Column(Boolean)
    is_media = Column(Boolean)
    options = Column(JSON)
    correct = Column(Integer)
    value = Column(Integer)

    def __init__(self, id, exam_id, question, type, options, correct):
        self.id = id
        self.exam_id = exam_id
        self.question = question
        self,is_written = is_written
        self,is_media = is_media
        self.options = options
        self.correct = correct
        self,value = value
