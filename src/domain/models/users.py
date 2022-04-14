from typing import Optional
from sqlmodel import SQLModel, Field


class UserBase(SQLModel):
    name: str = Field(default="")
    email: str = Field(default="")
    password: str = Field(default="")
    created_at: Optional[str] = Field(default=None)
    updated_at: Optional[str] = Field(default=None)
    deleted_at: Optional[str] = Field(default=None)
