from sqlmodel import create_engine, Session, SQLModel


class DBConnectionHandler:
    def __init__(self):
        self.__connection_string = "sqlite:///database.db"
        self.session = None

    def get_engine(self):
        return create_engine(self.__connection_string)

    def create_db_and_tables(self):
        engine = self.get_engine()
        SQLModel.metadata.create_all(engine)

    def __enter__(self):
        engine = self.get_engine()
        self.session = Session(engine)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
