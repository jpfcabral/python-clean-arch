from typing import Optional
from sqlmodel import Field
from src.infra.db.config import SQLModel


class Users(SQLModel, table=True):

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(default="")
    email: str = Field(default="")
    password: str = Field(default="")
    created_at: Optional[str] = Field(default=None)
    updated_at: Optional[str] = Field(default=None)
    deleted_at: Optional[str] = Field(default=None)

    def __rep__(self):
        return f"User [name={self.name}, email={self.email}]"
