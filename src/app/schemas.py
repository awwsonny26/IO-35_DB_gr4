from uuid import UUID
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field

class ProjectCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=64)
    description: Optional[str]

class ProjectUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=64)
    description: Optional[str]
    status: Optional[str] = Field(None, max_length=32)

class ProjectRead(BaseModel):
    id: UUID
    name: str
    description: Optional[str]
    creation_date: datetime
    status: str
    model_config = dict(from_attributes=True)

class BoardCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=64)

class BoardRead(BaseModel):
    id: UUID
    name: str
    project_id: UUID
    model_config = dict(from_attributes=True)

class BlockCreate(BaseModel):
    reason: str = Field(..., min_length=1)
    until_date: Optional[datetime]

class BlockRead(BaseModel):
    id: UUID
    project_id: UUID
    reason: str
    until_date: Optional[datetime]
    model_config = dict(from_attributes=True)
