from pydantic import BaseModel
from uuid import uuid4, UUID
from typing import Optional
from typing import List
'''
from enum import Enum

class ExamStateEnum(Enum):
    draft = 1
    active = 2
    obsolete = 3
'''
class ExamTemplate(BaseModel):
    id: UUID
    name: str
    course_id: UUID
    state: str#ExamStateEnum

class ExamTemplatePatch(BaseModel):
    name: Optional[str]
    state: Optional[str]
    state: Optional[str]

class ExamTemplateSchema(BaseModel):
    name: str
    course_id: UUID
    state: str
    state: str