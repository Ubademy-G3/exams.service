from pydantic import BaseModel
from uuid import UUID
from typing import Optional, List
import enum


class ExamStateEnum(enum.Enum):
    draft = 1
    active = 2
    inactive = 3


class ExamTemplatePostBody(BaseModel):
    course_id: UUID
    creator_id: UUID
    name: str


class ExamTemplateDB(BaseModel):
    id: UUID
    course_id: UUID
    creator_id: UUID
    name: str
    state: str
    max_score: float
    has_multiple_choice: bool
    has_written: bool
    has_media: bool
    max_attempts: int


class ExamTemplateList(BaseModel):
    course_id: UUID
    amount: int
    exam_templates: Optional[List[ExamTemplateDB]]


class CreatorExamTemplateList(BaseModel):
    creator_id: UUID
    amount: int
    exam_templates: Optional[List[ExamTemplateDB]]


class ExamTemplatePatch(BaseModel):
    name: Optional[str]
    state: Optional[str]
    max_score: Optional[float]
    has_multiple_choice: Optional[bool]
    has_written: Optional[bool]
    has_media: Optional[bool]
    max_attempts: Optional[int]
