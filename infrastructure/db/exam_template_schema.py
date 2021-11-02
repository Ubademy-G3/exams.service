from sqlalchemy import (Column, Integer, String, Table, MetaData, ForeignKey)
from sqlalchemy.dialects.postgresql import (UUID, ARRAY)
import uuid

metadata = MetaData()

exam_templates = Table(
    'exam_templates',
    metadata,
    Column('id', UUID, primary_key=True, default= uuid.uuid4),
    Column('name', String(50)),
    Column('course_id', UUID,  default= uuid.uuid4),
    Column('questions', ARRAY(UUID, ForeignKey('question_templates.id')))
    
)

#va eso de foreign key?