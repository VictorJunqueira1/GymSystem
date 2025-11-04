"""
Repositório de Treinos - Gerencia persistência de treinos
"""
from src.repositories.base_repository import BaseRepository
from src.entities.treino import Treino

class TreinoRepository(BaseRepository):
    def __init__(self, filepath: str = 'data/treinos.json'):
        super().__init__(filepath)
    
    def criar(self, treino: Treino) -> Treino:
        """Cria um novo treino"""
        data = self._read_data()
        treino.id = self._get_next_id(data)
        data.append(treino.to_dict())
        self._write_data(data)
        return treino
    
    def listar_todos(self) -> list:
        """Lista todos os treinos"""
        data = self._read_data()
        return [Treino.from_dict(item) for item in data]
    
    def buscar_por_id(self, id: int) -> Treino:
        """Busca treino por ID"""
        data = self._read_data()
        for item in data:
            if item['id'] == id:
                return Treino.from_dict(item)
        return None
    
    def buscar_por_nome(self, nome: str) -> list:
        """Busca treinos por nome (busca parcial)"""
        data = self._read_data()
        nome_lower = nome.lower()
        return [
            Treino.from_dict(item) 
            for item in data 
            if nome_lower in item['nome'].lower()
        ]
    
    def atualizar(self, treino: Treino) -> bool:
        """Atualiza um treino existente"""
        data = self._read_data()
        for i, item in enumerate(data):
            if item['id'] == treino.id:
                data[i] = treino.to_dict()
                self._write_data(data)
                return True
        return False
    
    def deletar(self, id: int) -> bool:
        """Deleta um treino"""
        data = self._read_data()
        for i, item in enumerate(data):
            if item['id'] == id:
                data.pop(i)
                self._write_data(data)
                return True
        return False
