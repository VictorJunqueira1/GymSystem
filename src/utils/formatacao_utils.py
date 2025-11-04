"""
Utilitários para formatação de dados
"""

def formatar_exercicio(exercicio) -> str:
    """Formata um exercício para exibição"""
    return f"ID: {exercicio.id} | {exercicio.nome} ({exercicio.tipo}) - {exercicio.repeticoes} reps"

def formatar_treino(treino) -> str:
    """Formata um treino para exibição"""
    desc = f" - {treino.descricao}" if treino.descricao else ""
    return f"ID: {treino.id} | {treino.nome}{desc} ({len(treino.exercicios)} exercícios)"

def formatar_exercicio_treino(dados: dict) -> str:
    """Formata um exercício dentro de um treino"""
    ex = dados['exercicio']
    series = dados['series']
    reps = dados['repeticoes']
    return f"  • {ex.nome} ({ex.tipo}) - {series}x{reps}"

def formatar_tabela(dados: list, colunas: list) -> str:
    """Formata dados em formato de tabela"""
    if not dados:
        return "Nenhum dado para exibir"
    
    # Calcula largura das colunas
    larguras = {col: len(col) for col in colunas}
    for item in dados:
        for col in colunas:
            valor = str(item.get(col, ''))
            larguras[col] = max(larguras[col], len(valor))
    
    # Cria cabeçalho
    linha_separadora = "+" + "+".join(["-" * (larguras[col] + 2) for col in colunas]) + "+"
    cabecalho = "|" + "|".join([f" {col.ljust(larguras[col])} " for col in colunas]) + "|"
    
    # Cria linhas de dados
    linhas = []
    for item in dados:
        linha = "|" + "|".join([f" {str(item.get(col, '')).ljust(larguras[col])} " for col in colunas]) + "|"
        linhas.append(linha)
    
    # Monta tabela
    tabela = [linha_separadora, cabecalho, linha_separadora]
    tabela.extend(linhas)
    tabela.append(linha_separadora)
    
    return "\n".join(tabela)
