import enum
from typing import Optional
from sqlmodel import SQLModel, Field
from sqlalchemy import Column, Enum


class AnimalType(enum.Enum):
    DOG = "dog"
    CAT = "cat"
    BIRD = "bird"
    OTHER = "other"


class PetBase(SQLModel):
    name: str = Field(default="")
    specie: AnimalType = Field(sa_column=Column(Enum(AnimalType)))
    age: int = Field(default=0)
    created_at: Optional[str] = Field(default=None)
    updated_at: Optional[str] = Field(default=None)
    deleted_at: Optional[str] = Field(default=None)
