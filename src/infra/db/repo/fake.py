from src.infra.db.config import DBConnectionHandler
from src.infra.db.entities import Users


class FakeRepo:
    @classmethod()
    def insert_user(cls, name: str, email: str, password: str):

        with DBConnectionHandler() as db_connection:
            try:
                user = Users(name=name, email=email, password=password)
                db_connection.session.add(user)
                db_connection.session.commit()
            except Exception as e:
                print(e)
                db_connection.session.rollback()
                raise e
            finally:
                db_connection.session.close()
