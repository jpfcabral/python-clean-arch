from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from src.infra.db.config import Base


class User(Base):

    __table__name = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    deleted_at = Column(DateTime)

    id_pet = relationship("Pets")

    def __rep__(self):
        return f"User [name={self.name}, email={self.email}]"
