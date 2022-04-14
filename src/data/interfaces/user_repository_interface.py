from abc import ABC, abstractmethod
from src.domain.models import UserBase


class UserRepositoryInterface(ABC):
    @abstractmethod
    def insert_user(self, name: str, email: str, password: str) -> UserBase:
        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def get_user_by_id(self, user_id: int) -> UserBase:
        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def delete_user_by_id(self, user_id: int) -> None:
        raise NotImplementedError("Method not implemented")
