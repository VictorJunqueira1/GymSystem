"""
Utilitários para menus e interface do usuário
"""

def limpar_tela():
    """Limpa a tela do console"""
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_titulo(titulo: str):
    """Exibe um título formatado"""
    print("\n" + "=" * 60)
    print(titulo.center(60))
    print("=" * 60 + "\n")

def exibir_mensagem(mensagem: str, tipo: str = "info"):
    """Exibe uma mensagem formatada"""
    simbolos = {
        "sucesso": "✓",
        "erro": "✗",
        "info": "ℹ",
        "aviso": "⚠"
    }
    simbolo = simbolos.get(tipo, "•")
    print(f"\n{simbolo} {mensagem}\n")

def pausar():
    """Pausa a execução até o usuário pressionar Enter"""
    input("\nPressione ENTER para continuar...")

def ler_inteiro(mensagem: str, minimo: int = None, maximo: int = None) -> int:
    """Lê um número inteiro com validação"""
    while True:
        try:
            valor = int(input(mensagem))
            if minimo is not None and valor < minimo:
                print(f"Valor deve ser maior ou igual a {minimo}")
                continue
            if maximo is not None and valor > maximo:
                print(f"Valor deve ser menor ou igual a {maximo}")
                continue
            return valor
        except ValueError:
            print("Por favor, digite um número válido")

def ler_texto(mensagem: str, obrigatorio: bool = True) -> str:
    """Lê um texto com validação"""
    while True:
        texto = input(mensagem).strip()
        if obrigatorio and not texto:
            print("Este campo é obrigatório")
            continue
        return texto

def confirmar(mensagem: str) -> bool:
    """Solicita confirmação do usuário"""
    resposta = input(f"{mensagem} (s/n): ").strip().lower()
    return resposta in ['s', 'sim', 'y', 'yes']
