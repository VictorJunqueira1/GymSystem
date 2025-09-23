from typing import List, Optional
from uuid import UUID

from app.application.dtos.exercise_dto import (CreateExerciseDTO, ExerciseDTO,
                                             UpdateExerciseDTO)
from app.application.mappers.exercise_mapper import ExerciseMapper
from app.domain.interfaces.exercise_repository import ExerciseRepository
from app.shared.errors import NotFoundError
from app.shared.result import Result


class ExerciseService:
    def __init__(self, repository: ExerciseRepository):
        self.repository = repository
        self.mapper = ExerciseMapper()

    def create_exercise(self, dto: CreateExerciseDTO) -> Result[ExerciseDTO]:
        try:
            exercise = self.mapper.to_entity(dto)
            created = self.repository.create(exercise)
            return Result.ok(self.mapper.to_dto(created))
        except ValueError as e:
            return Result.fail(str(e))
        except Exception as e:
            return Result.fail("Erro ao criar exercício")

    def get_exercise(self, exercise_id: UUID) -> Result[ExerciseDTO]:
        try:
            exercise = self.repository.get_by_id(exercise_id)
            if not exercise:
                return Result.fail(NotFoundError("Exercício não encontrado"))
            return Result.ok(self.mapper.to_dto(exercise))
        except Exception as e:
            return Result.fail("Erro ao buscar exercício")

    def list_exercises(self, search: Optional[str] = None, page: int = 1, size: int = 10) -> Result[List[ExerciseDTO]]:
        try:
            exercises = self.repository.get_all(search, page, size)
            return Result.ok([self.mapper.to_dto(ex) for ex in exercises])
        except Exception as e:
            return Result.fail("Erro ao listar exercícios")

    def update_exercise(self, exercise_id: UUID, dto: UpdateExerciseDTO) -> Result[ExerciseDTO]:
        try:
            exercise = self.repository.get_by_id(exercise_id)
            if not exercise:
                return Result.fail(NotFoundError("Exercício não encontrado"))

            updated = self.mapper.update_entity(exercise, dto)
            result = self.repository.update(updated)
            
            if not result:
                return Result.fail("Erro ao atualizar exercício")
                
            return Result.ok(self.mapper.to_dto(result))
        except ValueError as e:
            return Result.fail(str(e))
        except Exception as e:
            return Result.fail("Erro ao atualizar exercício")

    def delete_exercise(self, exercise_id: UUID) -> Result[bool]:
        try:
            if not self.repository.get_by_id(exercise_id):
                return Result.fail(NotFoundError("Exercício não encontrado"))

            deleted = self.repository.delete(exercise_id)
            if not deleted:
                return Result.fail("Erro ao deletar exercício")
                
            return Result.ok(True)
        except Exception as e:
            return Result.fail("Erro ao deletar exercício")