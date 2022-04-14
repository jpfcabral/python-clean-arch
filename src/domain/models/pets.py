import enum
from typing import Optional
from sqlmodel import SQLModel, Field


class AnimalType(enum.Enum):
    DOG = "dog"
    CAT = "cat"
    BIRD = "bird"
    OTHER = "other"


class PetBase(SQLModel):
    name: str = Field(default="")
    specie: str
    age: int = Field(default=0)
    created_at: Optional[str] = Field(default=None)
    updated_at: Optional[str] = Field(default=None)
    deleted_at: Optional[str] = Field(default=None)
