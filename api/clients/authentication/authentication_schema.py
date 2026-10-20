from pydantic import BaseModel, Field, EmailStr

from tools.api.fakers import fake


class LoginRequestSchema(BaseModel):
    email: EmailStr = Field(default_factory=fake.email())
    password: str = Field(default_factory=fake.password())


class TokenSchema(BaseModel):
    token_type: str = Field(alias="tokenType")
    access_token: str = Field(alias="accessToken")
    refresh_token: str = Field(alias="refreshToken")


class LoginResponseSchema(BaseModel):
    token: TokenSchema


class RefreshRequestSchema(BaseModel):
    refresh_token: str = Field(alias="refreshToken")


class RefreshResponseSchema(BaseModel):
    token: TokenSchema


class LogoutRequestSchema(BaseModel):
    access_token: str = Field(alias="accessToken")
    refresh_token: str = Field(alias="refreshToken")


class AuthenticationUserSchema(BaseModel, frozen=True):
    email: str
    password: str


class AuthenticatedUserSchema(BaseModel):
    authentication_user: AuthenticationUserSchema
    token: TokenSchema
