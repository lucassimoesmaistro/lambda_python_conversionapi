# domain/repositories.py

from abc import ABC, abstractmethod
from domain.entities import User

class UserRepository(ABC):
    @abstractmethod
    def create(self, user: User) -> User:
        pass
