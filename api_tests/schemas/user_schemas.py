from typing import List

from pydantic import BaseModel, EmailStr


class UserData(BaseModel):
    id: int
    email: EmailStr
    first_name: str
    last_name: str
    avatar: str


class Support(BaseModel):
    url: str
    text: str


class UserListResponse(BaseModel):
    page: int
    per_page: int
    total: int
    total_pages: int
    data: List[UserData]
    support: Support


class UserSingleResponse(BaseModel):
    data: UserData
    support: Support


class CreateUserResponse(BaseModel):
    first_name: str
    last_name: str
    id: str
    createdAt: str

class UpdateUserResponse(BaseModel):
    first_name: str
    last_name: str
    updatedAt: str