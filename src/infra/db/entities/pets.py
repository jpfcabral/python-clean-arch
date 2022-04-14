from typing import Optional
from sqlmodel import Field
from sqlalchemy import Column, Enum
from src.domain.models.pets import PetBase, AnimalType


class Pet(PetBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    specie: AnimalType = Field(sa_column=Column(Enum(AnimalType)))

    def __rep__(self):
        return f"Pets [name={self.name}, specie={self.specie}, age={self.age}]"
