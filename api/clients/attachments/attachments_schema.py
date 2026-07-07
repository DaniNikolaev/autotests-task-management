from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field, FilePath

from tools.api.fakers import fake


class AttachmentSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: str
    filename: str
    directory: str
    task_id: str = Field(alias="taskId")
    uploaded_by: str = Field(alias="uploadedBy")
    created_at: datetime = Field(alias="createdAt")
    url: str


class CreateAttachmentRequestSchema(BaseModel):
    filename: str = Field(default_factory=lambda: f'{fake.uuid4()}.jpg')
    directory: str = Field(default="tests")
    upload_file: FilePath


class CreateAttachmentResponseSchema(BaseModel):
    attachment: AttachmentSchema


class GetAttachmentResponseSchema(BaseModel):
    attachment: AttachmentSchema
