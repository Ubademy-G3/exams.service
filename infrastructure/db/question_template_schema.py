from sqlalchemy import (Column, Integer, String, Table, MetaData, ForeignKey)
from sqlalchemy.dialects.postgresql import (UUID, ARRAY)
import uuid

metadata = MetaData()

question_templates = Table(
    'question_templates',
    metadata,
    Column('id', UUID, primary_key=True, default= uuid.uuid4),
    Column('exam_id', UUID, ForeignKey('exam_templates.id')),
    Column('question', String(300)),
    Column('type', String(15)),
    Column('options', ARRAY(String(50))),
    Column('correct', Integer)
    
)