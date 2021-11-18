from infrastructure.db.database import Base
from sqlalchemy import (Column, Integer, String, Table, MetaData, ForeignKey, Boolean, Enum)
from sqlalchemy.dialects.postgresql import (UUID, ARRAY)
import uuid
#from domain.exam_template_model import ExamStateEnum
#from enum import Enum

class ExamTemplate(Base):
    
    __tablename__ = "exam_templates"
    id = Column(UUID(as_uuid=True), primary_key=True, nullable = False)
    name = Column(String(50), nullable = False)
    course_id = Column(UUID, nullable = False)
    state = Column(String(10), nullable = False)#Enum(ExamStateEnum))
    
    def __init__(self, id, name, course_id, state):
        self.id = id
        self.name = name
        self.course_id = course_id
        self.state = state

'''
metadata = MetaData()

exam_templates = Table(
    'exam_templates',
    metadata,
    Column('id', UUID, primary_key=True, default= uuid.uuid4),
    Column('name', String(50)),
    Column('course_id', UUID,  default= uuid.uuid4),
    Column('state', String(10))#Enum(ExamStateEnum))
)'''