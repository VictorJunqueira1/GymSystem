"""
Repositório de Exercícios - Gerencia persistência de exercícios
"""
from src.repositories.base_repository import BaseRepository
from src.entities.exercicio import Exercicio

class ExercicioRepository(BaseRepository):
    def __init__(self, filepath: str = 'data/exercicios.json'):
        super().__init__(filepath)
    
    def criar(self, exercicio: Exercicio) -> Exercicio:
        """Cria um novo exercício"""
        data = self._read_data()
        exercicio.id = self._get_next_id(data)
        data.append(exercicio.to_dict())
        self._write_data(data)
        return exercicio
    
    def listar_todos(self) -> list:
        """Lista todos os exercícios"""
        data = self._read_data()
        return [Exercicio.from_dict(item) for item in data]
    
    def buscar_por_id(self, id: int) -> Exercicio:
        """Busca exercício por ID"""
        data = self._read_data()
        for item in data:
            if item['id'] == id:
                return Exercicio.from_dict(item)
        return None
    
    def buscar_por_nome(self, nome: str) -> list:
        """Busca exercícios por nome (busca parcial)"""
        data = self._read_data()
        nome_lower = nome.lower()
        return [
            Exercicio.from_dict(item) 
            for item in data 
            if nome_lower in item['nome'].lower()
        ]
    
    def atualizar(self, exercicio: Exercicio) -> bool:
        """Atualiza um exercício existente"""
        data = self._read_data()
        for i, item in enumerate(data):
            if item['id'] == exercicio.id:
                data[i] = exercicio.to_dict()
                self._write_data(data)
                return True
        return False
    
    def deletar(self, id: int) -> bool:
        """Deleta um exercício"""
        data = self._read_data()
        for i, item in enumerate(data):
            if item['id'] == id:
                data.pop(i)
                self._write_data(data)
                return True
        return False
