import enum
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Enum
from src.infra.db.config import Base


class AnimalType(enum.Enum):
    DOG = "dog"
    CAT = "cat"
    BIRD = "bird"
    OTHER = "other"


class Pets(Base):

    __tablename__ = "pets"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    specie = Column(Enum(AnimalType), nullable=False)
    age = Column(Integer, nullable=False)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    deleted_at = Column(DateTime)

    user_id = Column(Integer, ForeignKey("users.id"))

    def __rep__(self):
        return f"Pets [name={self.name}, specie={self.specie}, age={self.age}]"
