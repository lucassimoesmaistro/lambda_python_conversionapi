from application.use_cases import CreateUserUseCase
from infrastructure.adapters import UserRepositoryImpl
from infrastructure.database import MysqlDatabase

def lambda_handler(event, context):
    database = MysqlDatabase(host="localhost", user="root", password="12345678", database="Users")
    user_repository = UserRepositoryImpl(database=database)
    create_user_use_case = CreateUserUseCase(user_repository)

    user = create_user_use_case.execute(name="John", email="john@example.com")

    return {
        "statusCode": 200,
        "body": str(user)
    }
