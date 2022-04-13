from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DBConnectionHandler:
    def __init__(self):
        self.__connection_string = "sqlite:///database.db"
        self.session = None

    def get_engine(self):
        return create_engine(self.__connection_string)

    def __enter__(self):
        engine = self.get_engine()
        session_maker = sessionmaker()
        self.session = session_maker(bind=engine)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
