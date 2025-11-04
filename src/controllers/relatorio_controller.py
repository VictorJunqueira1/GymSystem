"""
Controller de Relatórios - Camada intermediária para relatórios
"""
from src.services.relatorio_service import RelatorioService

class RelatorioController:
    def __init__(self, service: RelatorioService = None):
        self.service = service if service else RelatorioService()
    
    def listar_exercicios_treino(self, treino_id: int) -> dict:
        """Lista exercícios de um treino específico"""
        try:
            exercicios = self.service.listar_exercicios_do_treino(treino_id)
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
    
    def volume_treino(self, treino_id: int) -> dict:
        """Calcula o volume total de um treino"""
        try:
            volume = self.service.calcular_volume_treino(treino_id)
            return {
                'sucesso': True,
                'mensagem': 'Volume calculado com sucesso',
                'dados': volume
            }
        except ValueError as e:
            return {
                'sucesso': False,
                'mensagem': str(e),
                'dados': 0
            }
    
    def estatisticas(self) -> dict:
        """Retorna estatísticas gerais do sistema"""
        stats = self.service.estatisticas_gerais()
        return {
            'sucesso': True,
            'mensagem': 'Estatísticas geradas com sucesso',
            'dados': stats
        }
    
    def exercicios_populares(self) -> dict:
        """Retorna exercícios mais usados"""
        exercicios = self.service.exercicios_mais_usados()
        return {
            'sucesso': True,
            'mensagem': f'{len(exercicios)} exercício(s) encontrado(s)',
            'dados': exercicios
        }
