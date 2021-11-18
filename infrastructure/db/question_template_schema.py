from infrastructure.db.database import Base
from sqlalchemy import (Column, Integer, String, Table, MetaData, ForeignKey, JSON)
from sqlalchemy.dialects.postgresql import (UUID, ARRAY)
import uuid
#from domain.question_template_model import QuestionTypeEnum
#from enum import Enum

class QuestionTemplate(Base):
    __tablename__ = "question_templates"
    id = Column(UUID, primary_key=True, nullable = False)
    exam_id = Column(UUID, ForeignKey('exam_templates.id'), nullable = False)
    question = Column(String(300), nullable = False)
    type = Column(String(15), nullable = False)
    options = Column(JSON)
    correct = Column(Integer)

    def __init__(self, id, exam_id, question, type, options, correct):
        self.id = id
        self.exam_id = exam_id
        self.question = question
        self.type = type
        self.options = options
        self.correct = correct

'''
metadata = MetaData()

question_templates = Table(
    'question_templates',
    metadata,
    Column('id', UUID, primary_key=True, default= uuid.uuid4),
    Column('exam_id', UUID, ForeignKey('exam_templates.id')),
    Column('question', String(300)),
    Column('type', String(15)),#Enum(QuestionTypeEnum)),
    Column('options', JSON()),
    Column('correct', Integer)
    
)'''