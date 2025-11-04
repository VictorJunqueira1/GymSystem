"""
Serviço de Treinos - Implementa regras de negócio para treinos
"""
from src.repositories.treino_repository import TreinoRepository
from src.repositories.exercicio_repository import ExercicioRepository
from src.entities.treino import Treino, ExercicioTreino

class TreinoService:
    def __init__(self, treino_repository: TreinoRepository = None, exercicio_repository: ExercicioRepository = None):
        self.treino_repository = treino_repository if treino_repository else TreinoRepository()
        self.exercicio_repository = exercicio_repository if exercicio_repository else ExercicioRepository()
    
    def criar_treino(self, nome: str, descricao: str = "") -> Treino:
        """Cria um novo treino com validações"""
        if not nome or not nome.strip():
            raise ValueError("Nome do treino não pode ser vazio")
        
        treino = Treino(id=0, nome=nome.strip(), descricao=descricao.strip())
        return self.treino_repository.criar(treino)
    
    def listar_treinos(self) -> list:
        """Lista todos os treinos"""
        return self.treino_repository.listar_todos()
    
    def buscar_treino_por_id(self, id: int) -> Treino:
        """Busca treino por ID"""
        treino = self.treino_repository.buscar_por_id(id)
        if not treino:
            raise ValueError(f"Treino com ID {id} não encontrado")
        return treino
    
    def buscar_treinos_por_nome(self, nome: str) -> list:
        """Busca treinos por nome"""
        if not nome or not nome.strip():
            raise ValueError("Nome para busca não pode ser vazio")
        return self.treino_repository.buscar_por_nome(nome.strip())
    
    def atualizar_treino(self, id: int, nome: str = None, descricao: str = None) -> Treino:
        """Atualiza um treino existente"""
        treino = self.buscar_treino_por_id(id)
        
        if nome is not None:
            if not nome.strip():
                raise ValueError("Nome do treino não pode ser vazio")
            treino.nome = nome.strip()
        
        if descricao is not None:
            treino.descricao = descricao.strip()
        
        self.treino_repository.atualizar(treino)
        return treino
    
    def deletar_treino(self, id: int) -> bool:
        """Deleta um treino"""
        treino = self.buscar_treino_por_id(id)
        return self.treino_repository.deletar(treino.id)
    
    def adicionar_exercicio_ao_treino(self, treino_id: int, exercicio_id: int, series: int, repeticoes: int) -> Treino:
        """Adiciona um exercício a um treino"""
        treino = self.buscar_treino_por_id(treino_id)
        
        # Valida se o exercício existe
        exercicio = self.exercicio_repository.buscar_por_id(exercicio_id)
        if not exercicio:
            raise ValueError(f"Exercício com ID {exercicio_id} não encontrado")
        
        if series <= 0:
            raise ValueError("Séries devem ser maior que zero")
        
        if repeticoes <= 0:
            raise ValueError("Repetições devem ser maior que zero")
        
        # Verifica se o exercício já está no treino
        for ex in treino.exercicios:
            if ex.exercicio_id == exercicio_id:
                raise ValueError(f"Exercício {exercicio.nome} já está neste treino")
        
        exercicio_treino = ExercicioTreino(exercicio_id, series, repeticoes)
        treino.adicionar_exercicio(exercicio_treino)
        self.treino_repository.atualizar(treino)
        return treino
    
    def remover_exercicio_do_treino(self, treino_id: int, exercicio_id: int) -> Treino:
        """Remove um exercício de um treino"""
        treino = self.buscar_treino_por_id(treino_id)
        
        if not treino.remover_exercicio(exercicio_id):
            raise ValueError(f"Exercício com ID {exercicio_id} não encontrado neste treino")
        
        self.treino_repository.atualizar(treino)
        return treino
