from sqlalchemy import (Column, Integer, String, Table, MetaData, ForeignKey, JSON)
from sqlalchemy.dialects.postgresql import (UUID, ARRAY)
import uuid
#from domain.question_template_model import QuestionTypeEnum
#from enum import Enum

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
    
)