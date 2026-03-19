from pydantic import BaseModel


class RegisterResponse(BaseModel):
    id: int
    token: str


class LoginResponse(BaseModel):
    token: str


class AuthErrorResponse(BaseModel):
    error: str
