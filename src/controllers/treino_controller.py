"""
Controller de Treinos - Camada intermediária entre interface e serviços
"""
from src.services.treino_service import TreinoService

class TreinoController:
    def __init__(self, service: TreinoService = None):
        self.service = service if service else TreinoService()
    
    def criar(self, nome: str, descricao: str = "") -> dict:
        """Cria um novo treino"""
        try:
            treino = self.service.criar_treino(nome, descricao)
            return {
                'sucesso': True,
                'mensagem': 'Treino criado com sucesso',
                'dados': treino
            }
        except ValueError as e:
            return {
                'sucesso': False,
                'mensagem': str(e),
                'dados': None
            }
    
    def listar(self) -> dict:
        """Lista todos os treinos"""
        treinos = self.service.listar_treinos()
        return {
            'sucesso': True,
            'mensagem': f'{len(treinos)} treino(s) encontrado(s)',
            'dados': treinos
        }
    
    def buscar_por_nome(self, nome: str) -> dict:
        """Busca treinos por nome"""
        try:
            treinos = self.service.buscar_treinos_por_nome(nome)
            return {
                'sucesso': True,
                'mensagem': f'{len(treinos)} treino(s) encontrado(s)',
                'dados': treinos
            }
        except ValueError as e:
            return {
                'sucesso': False,
                'mensagem': str(e),
                'dados': []
            }
    
    def atualizar(self, id: int, nome: str = None, descricao: str = None) -> dict:
        """Atualiza um treino"""
        try:
            treino = self.service.atualizar_treino(id, nome, descricao)
            return {
                'sucesso': True,
                'mensagem': 'Treino atualizado com sucesso',
                'dados': treino
            }
        except ValueError as e:
            return {
                'sucesso': False,
                'mensagem': str(e),
                'dados': None
            }
    
    def deletar(self, id: int) -> dict:
        """Deleta um treino"""
        try:
            self.service.deletar_treino(id)
            return {
                'sucesso': True,
                'mensagem': 'Treino deletado com sucesso',
                'dados': None
            }
        except ValueError as e:
            return {
                'sucesso': False,
                'mensagem': str(e),
                'dados': None
            }
    
    def adicionar_exercicio(self, treino_id: int, exercicio_id: int, series: int, repeticoes: int) -> dict:
        """Adiciona um exercício ao treino"""
        try:
            treino = self.service.adicionar_exercicio_ao_treino(treino_id, exercicio_id, series, repeticoes)
            return {
                'sucesso': True,
                'mensagem': 'Exercício adicionado ao treino com sucesso',
                'dados': treino
            }
        except ValueError as e:
            return {
                'sucesso': False,
                'mensagem': str(e),
                'dados': None
            }
    
    def remover_exercicio(self, treino_id: int, exercicio_id: int) -> dict:
        """Remove um exercício do treino"""
        try:
            treino = self.service.remover_exercicio_do_treino(treino_id, exercicio_id)
            return {
                'sucesso': True,
                'mensagem': 'Exercício removido do treino com sucesso',
                'dados': treino
            }
        except ValueError as e:
            return {
                'sucesso': False,
                'mensagem': str(e),
                'dados': None
            }
