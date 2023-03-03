# application/use_cases.py
from domain.entities import User
from domain.repositories import UserRepository

class CreateUserUseCase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self, name: str, email: str) -> User:
        user = User(name=name, email=email)
        self.user_repository.create(user)
        return user
