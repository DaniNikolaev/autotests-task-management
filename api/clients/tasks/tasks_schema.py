from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

from tools.api.fakers import fake


class TaskSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: str
    title: str
    description: str
    status: str
    priority: str
    estimated_time: str = Field(alias="estimatedTime")
    related_project_id: str = Field(alias="relatedProjectId")
    created_by_user_id: str = Field(alias="createdByUserId")
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime | None = Field(alias="updatedAt")


class CreateTaskRequestSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    title: str = Field(default_factory=fake.sentence)
    description: str = Field(default_factory=fake.text)
    status: str = Field(default_factory=fake.task_status)
    priority: str = Field(default_factory=fake.task_priority)
    estimated_time: str = Field(alias="estimatedTime", default_factory=fake.estimated_time)


class CreateTaskResponseSchema(BaseModel):
    task: TaskSchema


class GetTaskResponseSchema(BaseModel):
    task: TaskSchema


class GetTasksResponseSchema(BaseModel):
    tasks: list[TaskSchema]


class UpdateTaskRequestSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    title: str = Field(default_factory=fake.sentence)
    description: str = Field(default_factory=fake.text)
    status: str = Field(default_factory=fake.task_status)
    priority: str = Field(default_factory=fake.task_priority)
    estimated_time: str = Field(alias="estimatedTime", default_factory=fake.estimated_time)


class UpdateTaskResponseSchema(BaseModel):
    task: TaskSchema
