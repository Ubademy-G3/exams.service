from sqlalchemy import (Column, Integer, String, Table, MetaData, ForeignKey, Boolean)
from sqlalchemy.dialects.postgresql import (UUID, ARRAY)
import uuid

metadata = MetaData()

exam_solutions = Table(
    'exam_solutions',
    metadata,
    Column('id', UUID, primary_key=True, default= uuid.uuid4),
    Column('name', String(50)),
    Column('course_id', UUID, default= uuid.uuid4),
    Column('user_id', UUID, default= uuid.uuid4),
    Column('graded', Boolean()),
    Column('score', Integer()),
    Column('aprobal_state', Boolean())
    
)

#va eso de foreign key?