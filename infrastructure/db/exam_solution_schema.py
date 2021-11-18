from infrastructure.db.database import Base
from sqlalchemy import (Column, Integer, String, Table, MetaData, ForeignKey, Boolean)
from sqlalchemy.dialects.postgresql import (UUID, ARRAY)
import uuid

class ExamSolution(Base):
    __tablename__ = "exam_solutions"
    id = Column(UUID, primary_key = True, nullable = False)
    name = Column(String(50), nullable = False)
    course_id = Column(UUID, nullable = False)
    user_id = Column(UUID, nullable = False)
    graded = Column(Boolean)
    score = Column(Integer)
    aprobal_state = Column(Boolean)

    def __init__(self, id, name, course_id, user_id, graded, score, aprobal_state):
        self.id = id
        self.name = name
        self.course_id = course_id
        self.user_id = user_id
        self.graded = graded
        self.score = score
        self.aprobal_state = aprobal_state
'''
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
    
)'''