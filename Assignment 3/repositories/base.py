from abc import ABC, abstractmethod
from typing import List, Optional, TypeVar, Generic

T = TypeVar("T")

class BaseRepository(ABC, Generic[T]):
    @abstractmethod
    def create(self, item: T) -> T:
        pass

    @abstractmethod
    def get(self, item_id: int) -> Optional[T]:
        pass

    @abstractmethod
    def get_all(self) -> List[T]:
        pass

    @abstractmethod
    def update(self, item_id: int, item: T) -> Optional[T]:
        pass

    @abstractmethod
    def delete(self, item_id: int) -> bool:
        pass
