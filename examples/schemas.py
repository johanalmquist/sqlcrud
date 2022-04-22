from typing import Optional

from pydantic import BaseModel


class UserCreate(BaseModel):
    name: str
    password: str


class UserUpdate(BaseModel):
    name: Optional[str]
    password: Optional[str]
