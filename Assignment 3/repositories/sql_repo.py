from sqlmodel import SQLModel, Session, select
from models.database import engine
from repositories.base import BaseRepository
from typing import List, Optional
from routes.patients import Patient  # Example: Adjust for other models

class SQLRepository(BaseRepository[Patient]):
    def create(self, item: Patient) -> Patient:
        with Session(engine) as session:
            session.add(item)
            session.commit()
            session.refresh(item)
            return item

    def get(self, item_id: int) -> Optional[Patient]:
        with Session(engine) as session:
            return session.get(Patient, item_id)

    def get_all(self) -> List[Patient]:
        with Session(engine) as session:
            return session.exec(select(Patient)).all()

    def update(self, item_id: int, item: Patient) -> Optional[Patient]:
        with Session(engine) as session:
            existing_item = session.get(Patient, item_id)
            if existing_item:
                for key, value in item.dict().items():
                    setattr(existing_item, key, value)
                session.commit()
                session.refresh(existing_item)
                return existing_item
        return None

    def delete(self, item_id: int) -> bool:
        with Session(engine) as session:
            existing_item = session.get(Patient, item_id)
            if existing_item:
                session.delete(existing_item)
                session.commit()
                return True
        return False
