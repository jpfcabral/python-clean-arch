from src.infra.db.config import DBConnectionHandler
from src.infra.db.entities import Pet
from src.data.interfaces import PetRepositoryInterface


class PetRepository(PetRepositoryInterface):
    @classmethod
    def insert_pet(cls, name: str, species: str) -> Pet:

        with DBConnectionHandler() as db_connection:
            try:
                pet = Pet(name=name, species=species)
                db_connection.session.add(pet)
                db_connection.session.commit()
                db_connection.session.refresh(pet)
                return pet
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
        return None

    @classmethod
    def get_pet_by_id(cls, pet_id: int) -> Pet:
        with DBConnectionHandler() as db_connection:
            try:
                pet = db_connection.session.query(Pet).filter(Pet.id == pet_id).first()
                return pet
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
        return None

    @classmethod
    def delete_pet_by_id(cls, pet_id: int) -> None:
        with DBConnectionHandler() as db_connection:
            try:
                pet = db_connection.session.query(Pet).filter(Pet.id == pet_id).first()
                db_connection.session.delete(pet)
                db_connection.session.commit()
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
        return None
