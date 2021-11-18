from infrastructure.db.database import Base
from sqlalchemy import (Column, Integer, String, Table, MetaData, ForeignKey, JSON)
from sqlalchemy.dialects.postgresql import (UUID, ARRAY)
import uuid

class QuestionSolution(Base):
    __tablename__ = "question_solutions"
    id = Column(UUID, primary_key=True, nullable = False)
    exam_id = Column(UUID, ForeignKey('exam_templates.id'), nullable = False)
    question = Column(String(300), nullable = False)
    type = Column(String(15), nullable = False)
    options = Column(JSON)
    correct = Column(Integer)
    user_id = Column(UUID, nullable = False)
    answer = Column(String(300), nullable = False)

    def __init__(self, id, exam_id, question, type, options, correct, user_id, answer):
        self.id = id
        self.exam_id = exam_id
        self.question = question
        self.type = type
        self.options = options
        self.correct = correct
        self.user_id = user_id
        self.answer = answer

'''
metadata = MetaData()

question_solutions = Table(
    'question_solutions',
    metadata,
    Column('id', UUID, primary_key=True, default= uuid.uuid4),
    Column('exam_id', UUID, ForeignKey('exam_templates.id')),
    Column('question', String(300)),
    Column('type', String(15)),
    Column('options', JSON()),
    Column('correct', Integer),
    Column('user_id', UUID, default= uuid.uuid4),
    Column('answer', String(300))
)'''