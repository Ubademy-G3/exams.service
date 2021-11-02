from sqlalchemy import (Column, Integer, String, Table, MetaData, ForeignKey)
from sqlalchemy.dialects.postgresql import (UUID, ARRAY)
import uuid

metadata = MetaData()

question_solutions = Table(
    'question_solutions',
    metadata,
    Column('id', UUID, primary_key=True, default= uuid.uuid4),
    Column('exam_id', UUID, ForeignKey('exam_templates.id')),
    Column('question', String(300)),
    Column('type', String(15)),
    Column('options', ARRAY(String(50))),
    Column('correct', Integer),
    Column('user_id', UUID, default= uuid.uuid4),
    Column('answer', String(300))
)