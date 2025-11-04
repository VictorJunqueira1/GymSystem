# Sistema de Gerenciamento de Treinos

Sistema completo para gerenciamento de treinos pessoais, desenvolvido em Python puro seguindo os princípios SOLID, DRY e KISS.

## 📋 Funcionalidades

### Gerenciamento de Exercícios
- ✅ Adicionar novos exercícios (nome, tipo, repetições)
- ✅ Listar todos os exercícios
- ✅ Buscar exercícios por nome
- ✅ Atualizar informações de exercícios
- ✅ Remover exercícios

### Gerenciamento de Treinos
- ✅ Criar treinos com nome e descrição
- ✅ Adicionar exercícios aos treinos (com séries e repetições)
- ✅ Listar todos os treinos
- ✅ Buscar treinos por nome
- ✅ Atualizar informações dos treinos
- ✅ Remover exercícios de treinos
- ✅ Remover treinos

### Relatórios
- ✅ Listar exercícios de um treino específico
- ✅ Calcular volume total de treino (séries × repetições)
- ✅ Estatísticas gerais do sistema
- ✅ Ranking de exercícios mais usados

## 🏗️ Arquitetura

O projeto segue uma arquitetura em camadas bem definida:

```
/src
 ├── entities/           # Classes de domínio
 │   ├── exercicio.py    # Entidade Exercicio
 │   └── treino.py       # Entidades Treino e ExercicioTreino
 │
 ├── repositories/       # Persistência de dados (JSON)
 │   ├── base_repository.py
 │   ├── exercicio_repository.py
 │   └── treino_repository.py
 │
 ├── services/          # Regras de negócio
 │   ├── exercicio_service.py
 │   ├── treino_service.py
 │   └── relatorio_service.py
 │
 ├── controllers/       # Camada intermediária
 │   ├── exercicio_controller.py
 │   ├── treino_controller.py
 │   └── relatorio_controller.py
 │
 ├── utils/            # Funções auxiliares
 │   ├── menu_utils.py
 │   └── formatacao_utils.py
 │
 └── main.py           # Ponto de entrada

/data                  # Arquivos JSON (criados automaticamente)
 ├── exercicios.json
 └── treinos.json
```

## 🎯 Princípios Aplicados

### SOLID
- **S**ingle Responsibility: Cada classe tem uma única responsabilidade
- **O**pen/Closed: Extensível através de herança (BaseRepository)
- **L**iskov Substitution: Repositórios podem ser substituídos
- **I**nterface Segregation: Interfaces específicas para cada domínio
- **D**ependency Inversion: Controllers dependem de abstrações (services)

### DRY (Don't Repeat Yourself)
- BaseRepository elimina duplicação de código de persistência
- Funções utilitárias reutilizáveis
- Métodos de conversão (to_dict/from_dict) nas entidades

### KISS (Keep It Simple, Stupid)
- Código limpo e legível
- Funções pequenas e focadas
- Sem dependências externas complexas

## 🚀 Como Executar

1. **Requisitos**: Python 3.6 ou superior

2. **Executar o sistema**:
```bash
    python -m src.main
```

3. **Estrutura de dados**: Os arquivos JSON serão criados automaticamente na pasta `data/`

## 📊 Exemplo de Uso

1. Adicione exercícios (ex: Supino, Agachamento, Rosca)
2. Crie um treino (ex: "Treino A - Peito e Tríceps")
3. Adicione exercícios ao treino com séries e repetições
4. Visualize relatórios e estatísticas

## 🔧 Tecnologias

- **Python 3**: Linguagem principal
- **JSON**: Armazenamento de dados
- **Bibliotecas built-in**: json, os (sem frameworks externos)

## 📝 Validações Implementadas

- Campos obrigatórios não podem ser vazios
- Valores numéricos devem ser positivos
- Exercícios não podem ser duplicados em um treino
- Verificação de existência antes de operações
- Confirmação para operações destrutivas

## 🎨 Interface

Interface de linha de comando (CLI) intuitiva com:
- Menus organizados por funcionalidade
- Mensagens de sucesso/erro formatadas
- Listagens claras e organizadas
- Confirmações para operações críticas

---

**Desenvolvido seguindo as melhores práticas de engenharia de software**
