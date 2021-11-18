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
    max_score = Column(Integer)
    has_multiple_choice = Column(Boolean)
    has_written = Column(Boolean)
    has_media = Column(Boolean)
    
    def __init__(self, id, name, course_id, state, max_score, has_multiple_choice, has_written, has_media):
        self.id = id
        self.name = name
        self.course_id = course_id
        self.state = state
        self.max_score = max_score
        self.has_multiple_choice = has_multiple_choice
        self.has_written = has_written
        self.has_media = has_media
        