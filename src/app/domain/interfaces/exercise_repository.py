from abc import ABC, abstractmethod
from typing import List, Optional
from uuid import UUID

from app.domain.entities.exercise import Exercise


class ExerciseRepository(ABC):
    @abstractmethod
    def create(self, exercise: Exercise) -> Exercise:
        pass

    @abstractmethod
    def get_by_id(self, exercise_id: UUID) -> Optional[Exercise]:
        pass

    @abstractmethod
    def get_all(self, search: Optional[str] = None, page: int = 1, size: int = 10) -> List[Exercise]:
        pass

    @abstractmethod
    def update(self, exercise: Exercise) -> Exercise:
        pass

    @abstractmethod
    def delete(self, exercise_id: UUID) -> bool:
        pass