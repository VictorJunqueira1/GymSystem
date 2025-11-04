"""
Entidade Treino - Representa um treino no sistema
"""

class ExercicioTreino:
    def __init__(self, exercicio_id: int, series: int, repeticoes: int):
        self.exercicio_id = exercicio_id
        self.series = series
        self.repeticoes = repeticoes
    
    def to_dict(self) -> dict:
        return {
            'exercicio_id': self.exercicio_id,
            'series': self.series,
            'repeticoes': self.repeticoes
        }
    
    @staticmethod
    def from_dict(data: dict) -> 'ExercicioTreino':
        return ExercicioTreino(
            exercicio_id=data['exercicio_id'],
            series=data['series'],
            repeticoes=data['repeticoes']
        )


class Treino:
    def __init__(self, id: int, nome: str, descricao: str = "", exercicios: list = None):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.exercicios = exercicios if exercicios else []
    
    def adicionar_exercicio(self, exercicio_treino: ExercicioTreino):
        """Adiciona um exercício ao treino"""
        self.exercicios.append(exercicio_treino)
    
    def remover_exercicio(self, exercicio_id: int) -> bool:
        """Remove um exercício do treino"""
        for i, ex in enumerate(self.exercicios):
            if ex.exercicio_id == exercicio_id:
                self.exercicios.pop(i)
                return True
        return False
    
    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'nome': self.nome,
            'descricao': self.descricao,
            'exercicios': [ex.to_dict() for ex in self.exercicios]
        }
    
    @staticmethod
    def from_dict(data: dict) -> 'Treino':
        exercicios = [ExercicioTreino.from_dict(ex) for ex in data.get('exercicios', [])]
        return Treino(
            id=data['id'],
            nome=data['nome'],
            descricao=data.get('descricao', ''),
            exercicios=exercicios
        )
    
    def __str__(self) -> str:
        return f"Treino(id={self.id}, nome='{self.nome}', exercicios={len(self.exercicios)})"
