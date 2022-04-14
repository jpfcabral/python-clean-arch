from typing import List
from src.infra.db.config import DBConnectionHandler
from src.infra.db.entities import User
from src.data.interfaces import UserRepositoryInterface


class UserRepository(UserRepositoryInterface):
    @classmethod
    def insert_user(cls, name: str, email: str, password: str) -> User:

        with DBConnectionHandler() as db_connection:
            try:
                user = User(name=name, email=email, password=password)
                db_connection.session.add(user)
                db_connection.session.commit()
                db_connection.session.refresh(user)
                return user
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
        return None

    @classmethod
    def get_user_by_id(cls, user_id: int) -> User:
        with DBConnectionHandler() as db_connection:
            try:
                user = (
                    db_connection.session.query(User).filter(User.id == user_id).first()
                )
                return user
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
        return None

    @classmethod
    def delete_user_by_id(cls, user_id: int) -> None:
        with DBConnectionHandler() as db_connection:
            try:
                user = (
                    db_connection.session.query(User).filter(User.id == user_id).first()
                )
                db_connection.session.delete(user)
                db_connection.session.commit()
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
        return None

    @classmethod
    def get_users_by_name(cls, name: str) -> List[User]:
        with DBConnectionHandler() as db_connection:
            try:
                users = (
                    db_connection.session.query(User).filter(User.name == name).all()
                )
                return users
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
        return None

    @classmethod
    def get_users_by_email(cls, email: str) -> List[User]:
        with DBConnectionHandler() as db_connection:
            try:
                users = (
                    db_connection.session.query(User).filter(User.email == email).all()
                )
                return users
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
        return None

    @classmethod
    def select_user(
        cls, id: int = None, name: str = None, email: str = None
    ) -> List[User]:
        with DBConnectionHandler() as db_connection:
            try:
                users = db_connection.session.query(User)
                if id:
                    users = users.filter(User.id == id)
                if name:
                    users = users.filter(User.name == name)
                if email:
                    users = users.filter(User.email == email)
                users = users.all()
                return users
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
        return None
