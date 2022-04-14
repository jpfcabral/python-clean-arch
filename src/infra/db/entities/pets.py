from typing import Optional
from sqlmodel import Field
from src.domain.models.pets import PetBase


class Pet(PetBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    def __rep__(self):
        return f"Pets [name={self.name}, specie={self.specie}, age={self.age}]"
