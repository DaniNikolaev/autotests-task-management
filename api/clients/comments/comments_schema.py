from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

from tools.api.fakers import fake


class CommentSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: str
    content: str
    is_edited: bool = Field(alias="isEdited")
    related_task_id: str = Field(alias="relatedTaskId")
    author_user_id: str = Field(alias="authorUserId")
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime | None = Field(alias="updatedAt")


class CreateCommentRequestSchema(BaseModel):
    content: str = Field(default_factory=fake.sentence)


class CreateCommentResponseSchema(BaseModel):
    comment: CommentSchema


class UpdateCommentRequestSchema(BaseModel):
    content: str = Field(default_factory=fake.sentence)


class UpdateCommentResponseSchema(BaseModel):
    comment: CommentSchema


class GetCommentsResponseSchema(BaseModel):
    comments: list[CommentSchema]


class GetCommentResponseSchema(BaseModel):
    comment: CommentSchema
