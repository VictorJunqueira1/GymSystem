"""
Serviço de Relatórios - Gera relatórios e estatísticas do sistema
"""
from src.repositories.treino_repository import TreinoRepository
from src.repositories.exercicio_repository import ExercicioRepository

class RelatorioService:
    def __init__(self, treino_repository: TreinoRepository = None, exercicio_repository: ExercicioRepository = None):
        self.treino_repository = treino_repository if treino_repository else TreinoRepository()
        self.exercicio_repository = exercicio_repository if exercicio_repository else ExercicioRepository()
    
    def listar_exercicios_do_treino(self, treino_id: int) -> list:
        """Lista todos os exercícios de um treino específico com detalhes"""
        treino = self.treino_repository.buscar_por_id(treino_id)
        if not treino:
            raise ValueError(f"Treino com ID {treino_id} não encontrado")
        
        resultado = []
        for ex_treino in treino.exercicios:
            exercicio = self.exercicio_repository.buscar_por_id(ex_treino.exercicio_id)
            if exercicio:
                resultado.append({
                    'exercicio': exercicio,
                    'series': ex_treino.series,
                    'repeticoes': ex_treino.repeticoes
                })
        
        return resultado
    
    def calcular_volume_treino(self, treino_id: int) -> int:
        """Calcula o volume total de um treino (séries x repetições)"""
        exercicios = self.listar_exercicios_do_treino(treino_id)
        volume_total = sum(ex['series'] * ex['repeticoes'] for ex in exercicios)
        return volume_total
    
    def estatisticas_gerais(self) -> dict:
        """Retorna estatísticas gerais do sistema"""
        exercicios = self.exercicio_repository.listar_todos()
        treinos = self.treino_repository.listar_todos()
        
        # Conta tipos de exercícios
        tipos_exercicios = {}
        for ex in exercicios:
            tipos_exercicios[ex.tipo] = tipos_exercicios.get(ex.tipo, 0) + 1
        
        # Conta exercícios por treino
        total_exercicios_treinos = sum(len(t.exercicios) for t in treinos)
        media_exercicios = total_exercicios_treinos / len(treinos) if treinos else 0
        
        return {
            'total_exercicios': len(exercicios),
            'total_treinos': len(treinos),
            'tipos_exercicios': tipos_exercicios,
            'media_exercicios_por_treino': round(media_exercicios, 2)
        }
    
    def exercicios_mais_usados(self) -> list:
        """Retorna os exercícios mais usados nos treinos"""
        treinos = self.treino_repository.listar_todos()
        contagem = {}
        
        for treino in treinos:
            for ex_treino in treino.exercicios:
                contagem[ex_treino.exercicio_id] = contagem.get(ex_treino.exercicio_id, 0) + 1
        
        # Ordena por uso
        exercicios_ordenados = sorted(contagem.items(), key=lambda x: x[1], reverse=True)
        
        resultado = []
        for exercicio_id, uso in exercicios_ordenados:
            exercicio = self.exercicio_repository.buscar_por_id(exercicio_id)
            if exercicio:
                resultado.append({
                    'exercicio': exercicio,
                    'uso': uso
                })
        
        return resultado
