"""
Repositório Base - Implementa operações genéricas de leitura/escrita em JSON
"""
import json
import os

class BaseRepository:
    def __init__(self, filepath: str):
        self.filepath = filepath
        self._ensure_file_exists()
    
    def _ensure_file_exists(self):
        """Garante que o arquivo e diretório existam"""
        os.makedirs(os.path.dirname(self.filepath), exist_ok=True)
        if not os.path.exists(self.filepath):
            self._write_data([])
    
    def _read_data(self) -> list:
        """Lê dados do arquivo JSON"""
        try:
            with open(self.filepath, 'r', encoding='utf-8') as file:
                return json.load(file)
        except (json.JSONDecodeError, FileNotFoundError):
            return []
    
    def _write_data(self, data: list):
        """Escreve dados no arquivo JSON"""
        with open(self.filepath, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)
    
    def _get_next_id(self, data: list) -> int:
        """Gera o próximo ID disponível"""
        if not data:
            return 1
        return max(item['id'] for item in data) + 1
