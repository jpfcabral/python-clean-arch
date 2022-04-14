from faker import Faker
from src.infra.db.config import DBConnectionHandler
from src.infra.db.repo.user_repository import UserRepository

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


def test_select_user():
    db_connection_handler.create_db_and_tables()

    name = fake.name()
    email = fake.email()
    password = fake.word()

    user = user_repository.insert_user(name, email, password)

    query_user1 = user_repository.get_user_by_id(user.id)
    query_user2 = user_repository.get_users_by_email(user.email)
    query_user3 = user_repository.get_users_by_name(user.name)

    assert user == query_user1
    assert user in query_user2
    assert user in query_user3

    query_user4 = user_repository.select_user(id=user.id)
    query_user5 = user_repository.select_user(email=user.email)
    query_user6 = user_repository.select_user(name=user.name)

    assert user in query_user4
    assert user in query_user5
    assert user in query_user6

    user_repository.delete_user_by_id(user_id=user.id)
