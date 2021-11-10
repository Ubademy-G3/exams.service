from pydantic import BaseModel
from uuid import uuid4, UUID
from typing import Optional

class ExamTemplate(BaseModel):
    id: UUID = uuid4()
    name: str
    course_id: UUID
    active: bool = True

class ExamTemplatePatch(BaseModel):
    name: Optional[str]
    course_id: Optional[UUID]

class ExamTemplateSchema(BaseModel):
    name: str
    course_id: UUID