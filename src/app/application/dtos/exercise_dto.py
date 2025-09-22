from dataclasses import dataclass
from typing import Optional
from uuid import UUID


@dataclass
class CreateExerciseDTO:
    name: str
    type: str
    min_repetitions: Optional[int] = None
    description: Optional[str] = None


@dataclass
class UpdateExerciseDTO:
    name: Optional[str] = None
    type: Optional[str] = None
    min_repetitions: Optional[int] = None
    description: Optional[str] = None


@dataclass
class ExerciseDTO:
    id: UUID
    name: str
    type: str
    min_repetitions: Optional[int]
    description: Optional[str]