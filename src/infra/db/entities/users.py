from typing import Optional
from sqlmodel import Field
from src.domain.models.users import UserBase


class User(UserBase, table=True):

    id: Optional[int] = Field(default=None, primary_key=True)

    def __rep__(self):
        return f"User [name={self.name}, email={self.email}]"
