from pydantic import BaseModel
from uuid import UUID
from typing import Optional, List
import enum
from sqlalchemy import Enum as SQLalchemyEnum


class ExamStateEnum(enum.Enum):
    draft = 1
    active = 2
    inactive = 3


class ExamTemplatePostBody(BaseModel):
    name: str
    course_id: UUID


class ExamTemplateDB(BaseModel):
    id: UUID
    name: str
    course_id: UUID
    state: str
    max_score: float
    has_multiple_choice: bool
    has_written: bool
    has_media: bool


class ExamTemplateList(BaseModel):
    amount: int
    course_id: UUID
    exam_templates: Optional[List[ExamTemplateDB]]


class ExamTemplatePatch(BaseModel):
    name: Optional[str]
    state: Optional[str]
    max_score: Optional[float]
    has_multiple_choice: Optional[bool]
    has_written: Optional[bool]
    has_media: Optional[bool]
