from typing import List

from pydantic import BaseModel


class JobCategoryBase(BaseModel):
    category: str


class JobCategoryCreate(JobCategoryBase):
    pass


class JobCategory(JobCategoryBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int
    is_active: bool
    categories: List[JobCategory] = []

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenPayload(BaseModel):
    sub: int
