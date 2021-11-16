from sqlalchemy import (Column, Integer, String, Table, MetaData, ForeignKey, Boolean, Enum)
from sqlalchemy.dialects.postgresql import (UUID, ARRAY)
import uuid
#from domain.exam_template_model import ExamStateEnum
#from enum import Enum

metadata = MetaData()

exam_templates = Table(
    'exam_templates',
    metadata,
    Column('id', UUID, primary_key=True, default= uuid.uuid4),
    Column('name', String(50)),
    Column('course_id', UUID,  default= uuid.uuid4),
    Column('state', String(10))#Enum(ExamStateEnum))
)