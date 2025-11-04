"""
Serviço de Exercícios - Implementa regras de negócio para exercícios
"""
from src.repositories.exercicio_repository import ExercicioRepository
from src.entities.exercicio import Exercicio

class ExercicioService:
    def __init__(self, repository: ExercicioRepository = None):
        self.repository = repository if repository else ExercicioRepository()
    
    def criar_exercicio(self, nome: str, tipo: str, repeticoes: int) -> Exercicio:
        """Cria um novo exercício com validações"""
        if not nome or not nome.strip():
            raise ValueError("Nome do exercício não pode ser vazio")
        
        if not tipo or not tipo.strip():
            raise ValueError("Tipo do exercício não pode ser vazio")
        
        if repeticoes <= 0:
            raise ValueError("Repetições devem ser maior que zero")
        
        exercicio = Exercicio(id=0, nome=nome.strip(), tipo=tipo.strip(), repeticoes=repeticoes)
        return self.repository.criar(exercicio)
    
    def listar_exercicios(self) -> list:
        """Lista todos os exercícios"""
        return self.repository.listar_todos()
    
    def buscar_exercicio_por_id(self, id: int) -> Exercicio:
        """Busca exercício por ID"""
        exercicio = self.repository.buscar_por_id(id)
        if not exercicio:
            raise ValueError(f"Exercício com ID {id} não encontrado")
        return exercicio
    
    def buscar_exercicios_por_nome(self, nome: str) -> list:
        """Busca exercícios por nome"""
        if not nome or not nome.strip():
            raise ValueError("Nome para busca não pode ser vazio")
        return self.repository.buscar_por_nome(nome.strip())
    
    def atualizar_exercicio(self, id: int, nome: str = None, tipo: str = None, repeticoes: int = None) -> Exercicio:
        """Atualiza um exercício existente"""
        exercicio = self.buscar_exercicio_por_id(id)
        
        if nome is not None:
            if not nome.strip():
                raise ValueError("Nome do exercício não pode ser vazio")
            exercicio.nome = nome.strip()
        
        if tipo is not None:
            if not tipo.strip():
                raise ValueError("Tipo do exercício não pode ser vazio")
            exercicio.tipo = tipo.strip()
        
        if repeticoes is not None:
            if repeticoes <= 0:
                raise ValueError("Repetições devem ser maior que zero")
            exercicio.repeticoes = repeticoes
        
        self.repository.atualizar(exercicio)
        return exercicio
    
    def deletar_exercicio(self, id: int) -> bool:
        """Deleta um exercício"""
        exercicio = self.buscar_exercicio_por_id(id)
        return self.repository.deletar(exercicio.id)
