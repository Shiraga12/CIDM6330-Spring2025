from typing import List, Optional
from repositories.base import BaseRepository
from routes.patients import Patient  # Example: Adjust for other models

class InMemoryRepository(BaseRepository[Patient]):
    def __init__(self):
        self.items = []

    def create(self, item: Patient) -> Patient:
        self.items.append(item)
        return item

    def get(self, item_id: int) -> Optional[Patient]:
        return next((item for item in self.items if item.id == item_id), None)

    def get_all(self) -> List[Patient]:
        return self.items

    def update(self, item_id: int, item: Patient) -> Optional[Patient]:
        for i, existing_item in enumerate(self.items):
            if existing_item.id == item_id:
                self.items[i] = item
                return item
        return None

    def delete(self, item_id: int) -> bool:
        for i, item in enumerate(self.items):
            if item.id == item_id:
                del self.items[i]
                return True
        return False
