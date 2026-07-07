from datetime import datetime

from pydantic import BaseModel, Field, EmailStr, ConfigDict, UUID4

from tools.api.fakers import fake


class UserSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID4
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    created_at: datetime = Field(alias="createdAt")
    update_at: datetime | None = Field(alias="updatedAt")
    is_active: bool = Field(alias="isActive")


class CreateUserRequestSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    email: EmailStr = Field(default_factory=fake.email)
    password: str = Field(default_factory=fake.password)
    last_name: str = Field(alias="lastName", default_factory=fake.last_name)
    first_name: str = Field(alias="firstName", default_factory=fake.first_name)


class CreateUserResponseSchema(BaseModel):
    user: UserSchema


class GetUserResponseSchema(BaseModel):
    user: UserSchema


class UpdateUserRequestSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    email: str | None = Field(default_factory=fake.email)
    password: str | None = Field(default_factory=fake.password)
    last_name: str | None = Field(alias="lastName", default_factory=fake.last_name)
    first_name: str | None = Field(alias="firstName", default_factory=fake.first_name)


class UpdateUserResponseSchema(BaseModel):
    user: UserSchema
    