from dataclasses import dataclass
from typing import Optional
from uuid import UUID, uuid4


@dataclass
class Exercise:
    name: str
    type: str
    min_repetitions: Optional[int]
    description: Optional[str]
    id: UUID = uuid4()

    def __post_init__(self):
        self._validate()

    def _validate(self):
        if not self.name or len(self.name.strip()) == 0:
            raise ValueError("Nome do exercício é obrigatório")
        
        if not self.type or len(self.type.strip()) == 0:
            raise ValueError("Tipo do exercício é obrigatório")
        
        if self.min_repetitions is not None and self.min_repetitions < 0:
            raise ValueError("Número mínimo de repetições deve ser positivo")