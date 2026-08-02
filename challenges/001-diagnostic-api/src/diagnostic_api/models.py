from dataclasses import dataclass
from enum import StrEnum

from pydantic import BaseModel, Field


class TaskStatus(StrEnum):
    TODO = "todo"
    IN_PROGRESS = "in_progress"
    DONE = "done"


@dataclass
class Task:
    id: int
    title: str
    description: str | None
    priority: int
    status: TaskStatus


class TaskCreate(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    description: str | None = Field(default=None, max_length=500)
    priority: int = Field(default=3, ge=1, le=5)


class TaskUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=100)
    description: str | None = Field(default=None, max_length=500)
    priority: int | None = Field(default=None, ge=1, le=5)
    status: TaskStatus | None = None


class TaskResponse(BaseModel):
    id: int
    title: str
    description: str | None
    priority: int
    status: TaskStatus
