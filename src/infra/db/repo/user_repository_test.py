from faker import Faker
from src.infra.db.config import DBConnectionHandler
from .user_repository import UserRepository

fake = Faker()
user_repository = UserRepository()
db_connection_handler = DBConnectionHandler()


def test_insert_user():
    db_connection_handler.create_db_and_tables()

    name = fake.name()
    email = fake.email()
    password = fake.word()

    user = user_repository.insert_user(name, email, password)
    query_user = user_repository.get_user_by_id(user.id)

    assert user.name == query_user.name
    assert user.email == query_user.email
    assert user.password == query_user.password

    user_repository.delete_user_by_id(user_id=user.id)
