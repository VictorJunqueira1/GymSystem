from app.application.dtos.exercise_dto import CreateExerciseDTO, ExerciseDTO, UpdateExerciseDTO
from app.domain.entities.exercise import Exercise


class ExerciseMapper:
    @staticmethod
    def to_entity(dto: CreateExerciseDTO) -> Exercise:
        return Exercise(
            name=dto.name,
            type=dto.type,
            min_repetitions=dto.min_repetitions,
            description=dto.description
        )

    @staticmethod
    def to_dto(entity: Exercise) -> ExerciseDTO:
        return ExerciseDTO(
            id=entity.id,
            name=entity.name,
            type=entity.type,
            min_repetitions=entity.min_repetitions,
            description=entity.description
        )

    @staticmethod
    def update_entity(entity: Exercise, dto: UpdateExerciseDTO) -> Exercise:
        if dto.name is not None:
            entity.name = dto.name
        if dto.type is not None:
            entity.type = dto.type
        if dto.min_repetitions is not None:
            entity.min_repetitions = dto.min_repetitions
        if dto.description is not None:
            entity.description = dto.description
        
        entity._validate()
        return entity