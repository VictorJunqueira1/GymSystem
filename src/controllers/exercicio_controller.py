"""
Controller de Exercícios - Camada intermediária entre interface e serviços
"""
from src.services.exercicio_service import ExercicioService

class ExercicioController:
    def __init__(self, service: ExercicioService = None):
        self.service = service if service else ExercicioService()
    
    def criar(self, nome: str, tipo: str, repeticoes: int) -> dict:
        """Cria um novo exercício"""
        try:
            exercicio = self.service.criar_exercicio(nome, tipo, repeticoes)
            return {
                'sucesso': True,
                'mensagem': 'Exercício criado com sucesso',
                'dados': exercicio
            }
        except ValueError as e:
            return {
                'sucesso': False,
                'mensagem': str(e),
                'dados': None
            }
    
    def listar(self) -> dict:
        """Lista todos os exercícios"""
        exercicios = self.service.listar_exercicios()
        return {
            'sucesso': True,
            'mensagem': f'{len(exercicios)} exercício(s) encontrado(s)',
            'dados': exercicios
        }
    
    def buscar_por_nome(self, nome: str) -> dict:
        """Busca exercícios por nome"""
        try:
            exercicios = self.service.buscar_exercicios_por_nome(nome)
            return {
                'sucesso': True,
                'mensagem': f'{len(exercicios)} exercício(s) encontrado(s)',
                'dados': exercicios
            }
        except ValueError as e:
            return {
                'sucesso': False,
                'mensagem': str(e),
                'dados': []
            }
    
    def atualizar(self, id: int, nome: str = None, tipo: str = None, repeticoes: int = None) -> dict:
        """Atualiza um exercício"""
        try:
            exercicio = self.service.atualizar_exercicio(id, nome, tipo, repeticoes)
            return {
                'sucesso': True,
                'mensagem': 'Exercício atualizado com sucesso',
                'dados': exercicio
            }
        except ValueError as e:
            return {
                'sucesso': False,
                'mensagem': str(e),
                'dados': None
            }
    
    def deletar(self, id: int) -> dict:
        """Deleta um exercício"""
        try:
            self.service.deletar_exercicio(id)
            return {
                'sucesso': True,
                'mensagem': 'Exercício deletado com sucesso',
                'dados': None
            }
        except ValueError as e:
            return {
                'sucesso': False,
                'mensagem': str(e),
                'dados': None
            }
