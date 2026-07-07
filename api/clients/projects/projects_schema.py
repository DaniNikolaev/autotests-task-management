from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field, RootModel

from tools.api.fakers import fake


class ProjectSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: str
    title: str
    description: str
    owner_user_id: str = Field(alias="ownerUserId")
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime | None = Field(alias="updatedAt")


class GetProjectsResponseSchema(BaseModel):
    projects: list[ProjectSchema]


class CreateProjectRequestSchema(BaseModel):
    title: str = Field(default_factory=fake.sentence)
    description: str = Field(default_factory=fake.text)


class CreateProjectResponseSchema(BaseModel):
    project: ProjectSchema


class GetProjectResponseSchema(BaseModel):
    project: ProjectSchema


class UpdateProjectRequestSchema(BaseModel):
    title: str = Field(default_factory=fake.sentence)
    description: str = Field(default_factory=fake.text)


class UpdateProjectResponseSchema(BaseModel):
    project: ProjectSchema
