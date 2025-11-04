"""
Entidade Exercicio - Representa um exercício no sistema
"""

class Exercicio:
    def __init__(self, id: int, nome: str, tipo: str, repeticoes: int):
        self.id = id
        self.nome = nome
        self.tipo = tipo
        self.repeticoes = repeticoes
    
    def to_dict(self) -> dict:
        """Converte o objeto para dicionário"""
        return {
            'id': self.id,
            'nome': self.nome,
            'tipo': self.tipo,
            'repeticoes': self.repeticoes
        }
    
    @staticmethod
    def from_dict(data: dict) -> 'Exercicio':
        """Cria um objeto Exercicio a partir de um dicionário"""
        return Exercicio(
            id=data['id'],
            nome=data['nome'],
            tipo=data['tipo'],
            repeticoes=data['repeticoes']
        )
    
    def __str__(self) -> str:
        return f"Exercicio(id={self.id}, nome='{self.nome}', tipo='{self.tipo}', repeticoes={self.repeticoes})"
