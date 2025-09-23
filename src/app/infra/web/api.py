from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from urllib.parse import urlparse, parse_qs
from uuid import UUID

from app.infra.data.json_exercise_repository import JsonExerciseRepository
from app.domain.services.exercise_service import ExerciseService
from app.application.dtos.exercise_dto import CreateExerciseDTO, UpdateExerciseDTO

# Initialize service
repository = JsonExerciseRepository()
service = ExerciseService(repository)

class RequestHandler(BaseHTTPRequestHandler):
    def _send_response(self, status_code, data):
        self.send_response(status_code)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

    def _get_request_data(self):
        content_length = int(self.headers.get('Content-Length', 0))
        if content_length > 0:
            return json.loads(self.rfile.read(content_length))
        return None

    def _parse_id_from_path(self, path):
        parts = path.split('/')
        if len(parts) >= 3:
            try:
                return UUID(parts[2])
            except ValueError:
                return None
        return None

    def do_GET(self):
        parsed_url = urlparse(self.path)
        path = parsed_url.path
        query = parse_qs(parsed_url.query)

        if path == '/health':
            self._send_response(200, {"status": "healthy"})
            return

        if path == '/exercises':
            search = query.get('search', [None])[0]
            page = int(query.get('page', [1])[0])
            size = int(query.get('size', [10])[0])
            
            result = service.list_exercises(search, page, size)
            if result.success:
                self._send_response(200, [vars(ex) for ex in result.data])
            else:
                self._send_response(400, {"error": str(result.error)})
            return

        if path.startswith('/exercises/'):
            exercise_id = self._parse_id_from_path(path)
            if not exercise_id:
                self._send_response(400, {"error": "ID inválido"})
                return

            result = service.get_exercise(exercise_id)
            if result.success:
                self._send_response(200, vars(result.data))
            else:
                status_code = 404 if "não encontrado" in str(result.error).lower() else 400
                self._send_response(status_code, {"error": str(result.error)})
            return

        self._send_response(404, {"error": "Endpoint não encontrado"})

    def do_POST(self):
        if self.path == '/exercises':
            data = self._get_request_data()
            if not data:
                self._send_response(400, {"error": "Dados inválidos"})
                return

            result = service.create_exercise(CreateExerciseDTO(**data))
            if result.success:
                self._send_response(201, vars(result.data))
            else:
                self._send_response(400, {"error": str(result.error)})
            return

        self._send_response(404, {"error": "Endpoint não encontrado"})

    def do_PUT(self):
        if self.path.startswith('/exercises/'):
            exercise_id = self._parse_id_from_path(self.path)
            if not exercise_id:
                self._send_response(400, {"error": "ID inválido"})
                return

            data = self._get_request_data()
            if not data:
                self._send_response(400, {"error": "Dados inválidos"})
                return

            result = service.update_exercise(exercise_id, UpdateExerciseDTO(**data))
            if result.success:
                self._send_response(200, vars(result.data))
            else:
                status_code = 404 if "não encontrado" in str(result.error).lower() else 400
                self._send_response(status_code, {"error": str(result.error)})
            return

        self._send_response(404, {"error": "Endpoint não encontrado"})

    def do_DELETE(self):
        if self.path.startswith('/exercises/'):
            exercise_id = self._parse_id_from_path(self.path)
            if not exercise_id:
                self._send_response(400, {"error": "ID inválido"})
                return

            result = service.delete_exercise(exercise_id)
            if result.success:
                self._send_response(204, None)
            else:
                status_code = 404 if "não encontrado" in str(result.error).lower() else 400
                self._send_response(status_code, {"error": str(result.error)})
            return

        self._send_response(404, {"error": "Endpoint não encontrado"})

def run(host="localhost", port=8000):
    server = HTTPServer((host, port), RequestHandler)
    print(f"Servidor rodando em http://{host}:{port}")
    server.serve_forever()

if __name__ == "__main__":
    run()