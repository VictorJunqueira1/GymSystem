# GymSystem

### Sistema de gerenciamento de treinos via API HTTP

### 🎯 Visão Geral

- **Núcleos obrigatórios (rubrica do professor):**
    - **Exercícios:** CRUD + busca
    - **Treinos:** CRUD + busca
    - **Relatório:** listar exercícios de um treino
- **Extras sugeridos (Etapa 3):** Agendamento com treinador

### 🧱 Arquitetura & Padrões

- **Backend:** Python puro com servidor HTTP nativo
- **Banco de Dados:** JSON
- **DDD compacto:** módulos por (domain/application/infra)
- **Princípios:** DRY, KISS, SOLID

### 📋 Requisitos

- Python 3.8+

### 🚀 Como Executar

1. **Rodar a API:**
```bash
python -m app.infra.web.api
```

A API estará disponível em `http://localhost:8000`

### 📝 Documentação da API

#### Endpoints de Exercícios

##### Criar Exercício
```http
POST /exercises
```
```json
{
  "name": "Supino Reto",
  "type": "Peito",
  "min_repetitions": 8,
  "description": "Exercício para peitoral"
}
```

#### Listar Exercícios
```http
GET /exercises?search=&page=1&size=10
```
- `search`: Busca por nome (opcional)
- `page`: Número da página (padrão: 1)
- `size`: Itens por página (padrão: 10)

#### Buscar Exercício
```http
GET /exercises/{id}
```

#### Atualizar Exercício
```http
PUT /exercises/{id}
```
```json
{
  "name": "Supino Reto",
  "type": "Peito",
  "min_repetitions": 10,
  "description": "Exercício atualizado"
}
```

#### Deletar Exercício
```http
DELETE /exercises/{id}
```

### 🧪 Como Testar

1. **Primeiro, inicie o servidor:**
```powershell
python -m app.infra.web.api
```

2. **Em outro terminal PowerShell, teste os endpoints:**

**Listar Exercícios:**
```powershell
Invoke-RestMethod -Uri "http://localhost:8000/exercises" -Method Get
```

**Buscar por Nome:**
```powershell
Invoke-RestMethod -Uri "http://localhost:8000/exercises?search=Supino" -Method Get
```

**Criar Exercício:**
```powershell
$exercicio = @{
    name = "Flexão de Braço"
    type = "Peito"
    min_repetitions = 10
    description = "Exercício corporal para peitoral e tríceps"
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://localhost:8000/exercises" `
    -Method Post `
    -Body $exercicio `
    -ContentType "application/json"
```

### 📁 Estrutura do Projeto

```
src/
├── app/
│   ├── application/     # DTOs e Mappers
│   ├── domain/         # Entidades e Interfaces
│   ├── infra/         # Implementações e API
│   └── shared/        # Utilitários
└── data/
    └── exercises.json  # Banco de dados
```

### ✅ Critérios de Aceite

- [x] Criar/listar/atualizar/remover funcionam
- [x] Buscar por nome funciona (case-insensitive)
- [x] Salva e lê de exercises.json (arquivo existe e atualiza)
- [x] 200/400/404 bem tratados (mensagens simples em PT-BR)
- [ ] Página no Notion: "Como testar Exercícios" (com prints)
- [ ] Joel abre PR; Victor revisa e aprova

### Tarefas Joel

- [x] Implementar os endpoints acima ✅
  - POST /exercises (criar)
  - GET /exercises (listar)
  - GET /exercises?search= (buscar por nome)
  - PUT /exercises/:id (atualizar)
  - DELETE /exercises/:id (remover)
- [x] Criar seed inicial no exercises.json (10 exercícios reais)
- [x] Montar passo a passo no README (como rodar, como testar)
- [ ] Montar documentação no Notion com prints