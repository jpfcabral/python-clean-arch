from abc import ABC, abstractmethod
from src.domain.models import PetBase


class PetRepositoryInterface(ABC):
    @abstractmethod
    def insert_pet(self, name: str, species: str) -> PetBase:
        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def get_pet_by_id(self, pet_id: int) -> PetBase:
        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def delete_pet_by_id(self, pet_id: int) -> None:
        raise NotImplementedError("Method not implemented")
