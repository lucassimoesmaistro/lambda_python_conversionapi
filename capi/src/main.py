# main.py
import logging

from application.use_cases import CreateUserUseCase
from infrastructure.adapters import UserRepositoryImpl
from infrastructure.database import MysqlDatabase

if __name__ == "__main__":
    database = MysqlDatabase(host="localhost", user="root", password="123456", database="Users")
    user_repository = UserRepositoryImpl(database=database)
    create_user_use_case = CreateUserUseCase(user_repository)

    user = create_user_use_case.execute(name="John", email="john@example.com")
    logging.basicConfig(level=logging.INFO)

    logger = logging.getLogger(__name__)

    logger.info('A aplicação foi iniciada com sucesso.')
    
    print(user)
