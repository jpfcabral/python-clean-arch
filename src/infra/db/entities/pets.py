import enum
from typing import Optional
from sqlalchemy import Column, Enum
from sqlmodel import Field
from src.infra.db.config import SQLModel


class AnimalType(enum.Enum):
    DOG = "dog"
    CAT = "cat"
    BIRD = "bird"
    OTHER = "other"


class Pets(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(default="")
    specie: AnimalType = Field(sa_column=Column(Enum(AnimalType)))
    age: int = Field(default=0)
    created_at: Optional[str] = Field(default=None)
    updated_at: Optional[str] = Field(default=None)
    deleted_at: Optional[str] = Field(default=None)

    def __rep__(self):
        return f"Pets [name={self.name}, specie={self.specie}, age={self.age}]"
