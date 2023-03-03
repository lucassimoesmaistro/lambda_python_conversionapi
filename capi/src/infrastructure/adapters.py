# infrastructure/adapters.py

from domain.entities import User
from domain.repositories import UserRepository
from infrastructure.database import MysqlDatabase

class UserRepositoryImpl(UserRepository):
    def __init__(self, database: MysqlDatabase):
        self.db = database
        self.db.connect() 

    def create(self, user: User) -> User:
        query = f"INSERT INTO users (name, email) VALUES ('{user.name}', '{user.email}')"
        self.db.execute_update(query)
        return user
