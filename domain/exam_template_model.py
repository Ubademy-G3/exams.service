from pydantic import BaseModel
from uuid import uuid4, UUID
from typing import Optional, List
'''
from enum import Enum

class ExamStateEnum(Enum):
    draft = 1
    active = 2
    obsolete = 3
'''
'''
class ExamTemplate(BaseModel):
    id: UUID
    name: str
    course_id: UUID
    state: str#ExamStateEnum
'''
class ExamTemplateSchema(BaseModel):
    name: str
    course_id: UUID

class ExamTemplateDB(ExamTemplateSchema):
    id: UUID

class ExamTemplateList(BaseModel):
    amount: int
    course_id: UUID
    exam_templates: List[ExamTemplateDB]

class ExamTemplatePatch(BaseModel):
    name: Optional[str]
    state: Optional[str]
    max_score: Optional[int]
    has_multiple_choice: Optional[bool]
    has_written: Optional[bool]
    has_media: Optional[bool]
