import json
import os
from typing import Dict, List, Optional
from uuid import UUID

from app.domain.entities.exercise import Exercise
from app.domain.interfaces.exercise_repository import ExerciseRepository


class JsonExerciseRepository(ExerciseRepository):
    def __init__(self, file_path: str = "data/exercises.json"):
        self.file_path = file_path
        self._ensure_file_exists()

    def _ensure_file_exists(self):
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
        if not os.path.exists(self.file_path):
            with open(self.file_path, "w", encoding="utf-8") as f:
                json.dump([], f, ensure_ascii=False)

    def _read_all(self) -> List[Dict]:
        with open(self.file_path, "r", encoding="utf-8") as f:
            return json.load(f)

    def _write_all(self, exercises: List[Dict]):
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(exercises, f, ensure_ascii=False, indent=2)

    def _to_dict(self, exercise: Exercise) -> Dict:
        return {
            "id": str(exercise.id),
            "name": exercise.name,
            "type": exercise.type,
            "min_repetitions": exercise.min_repetitions,
            "description": exercise.description
        }

    def _from_dict(self, data: Dict) -> Exercise:
        return Exercise(
            id=UUID(data["id"]),
            name=data["name"],
            type=data["type"],
            min_repetitions=data["min_repetitions"],
            description=data["description"]
        )

    def create(self, exercise: Exercise) -> Exercise:
        exercises = self._read_all()
        exercise_dict = self._to_dict(exercise)
        exercises.append(exercise_dict)
        self._write_all(exercises)
        return exercise

    def get_by_id(self, exercise_id: UUID) -> Optional[Exercise]:
        exercises = self._read_all()
        exercise_dict = next(
            (ex for ex in exercises if UUID(ex["id"]) == exercise_id),
            None
        )
        return self._from_dict(exercise_dict) if exercise_dict else None

    def get_all(self, search: Optional[str] = None, page: int = 1, size: int = 10) -> List[Exercise]:
        exercises = self._read_all()
        
        if search:
            search = search.lower()
            exercises = [ex for ex in exercises if search in ex["name"].lower()]

        # Calculate pagination
        start = (page - 1) * size
        end = start + size
        paginated_exercises = exercises[start:end]

        return [self._from_dict(ex) for ex in paginated_exercises]

    def update(self, exercise: Exercise) -> Exercise:
        exercises = self._read_all()
        
        for i, ex in enumerate(exercises):
            if UUID(ex["id"]) == exercise.id:
                exercises[i] = self._to_dict(exercise)
                self._write_all(exercises)
                return exercise
                
        return None

    def delete(self, exercise_id: UUID) -> bool:
        exercises = self._read_all()
        initial_length = len(exercises)
        
        exercises = [ex for ex in exercises if UUID(ex["id"]) != exercise_id]
        
        if len(exercises) != initial_length:
            self._write_all(exercises)
            return True
            
        return False