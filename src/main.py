"""
Sistema de Gerenciamento de Treinos
Ponto de entrada principal do sistema
"""
from src.controllers.exercicio_controller import ExercicioController
from src.controllers.treino_controller import TreinoController
from src.controllers.relatorio_controller import RelatorioController
from src.utils.menu_utils import *
from src.utils.formatacao_utils import *

class SistemaGerenciamentoTreinos:
    def __init__(self):
        self.exercicio_controller = ExercicioController()
        self.treino_controller = TreinoController()
        self.relatorio_controller = RelatorioController()
    
    def menu_principal(self):
        """Exibe o menu principal"""
        while True:
            limpar_tela()
            exibir_titulo("SISTEMA DE GERENCIAMENTO DE TREINOS")
            print("1. Gerenciar Exercícios")
            print("2. Gerenciar Treinos")
            print("3. Relatórios")
            print("0. Sair")
            
            opcao = ler_inteiro("\nEscolha uma opção: ", 0, 3)
            
            if opcao == 1:
                self.menu_exercicios()
            elif opcao == 2:
                self.menu_treinos()
            elif opcao == 3:
                self.menu_relatorios()
            elif opcao == 0:
                exibir_mensagem("Encerrando sistema...", "info")
                break
    
    def menu_exercicios(self):
        """Menu de gerenciamento de exercícios"""
        while True:
            limpar_tela()
            exibir_titulo("GERENCIAR EXERCÍCIOS")
            print("1. Adicionar Exercício")
            print("2. Listar Exercícios")
            print("3. Buscar Exercício por Nome")
            print("4. Atualizar Exercício")
            print("5. Remover Exercício")
            print("0. Voltar")
            
            opcao = ler_inteiro("\nEscolha uma opção: ", 0, 5)
            
            if opcao == 1:
                self.adicionar_exercicio()
            elif opcao == 2:
                self.listar_exercicios()
            elif opcao == 3:
                self.buscar_exercicio()
            elif opcao == 4:
                self.atualizar_exercicio()
            elif opcao == 5:
                self.remover_exercicio()
            elif opcao == 0:
                break
    
    def adicionar_exercicio(self):
        """Adiciona um novo exercício"""
        limpar_tela()
        exibir_titulo("ADICIONAR EXERCÍCIO")
        
        nome = ler_texto("Nome do exercício: ")
        tipo = ler_texto("Tipo (ex: Peito, Costas, Pernas): ")
        repeticoes = ler_inteiro("Repetições padrão: ", minimo=1)
        
        resultado = self.exercicio_controller.criar(nome, tipo, repeticoes)
        
        if resultado['sucesso']:
            exibir_mensagem(resultado['mensagem'], "sucesso")
            print(formatar_exercicio(resultado['dados']))
        else:
            exibir_mensagem(resultado['mensagem'], "erro")
        
        pausar()
    
    def listar_exercicios(self):
        """Lista todos os exercícios"""
        limpar_tela()
        exibir_titulo("LISTA DE EXERCÍCIOS")
        
        resultado = self.exercicio_controller.listar()
        
        if resultado['dados']:
            for exercicio in resultado['dados']:
                print(formatar_exercicio(exercicio))
        else:
            exibir_mensagem("Nenhum exercício cadastrado", "info")
        
        pausar()
    
    def buscar_exercicio(self):
        """Busca exercícios por nome"""
        limpar_tela()
        exibir_titulo("BUSCAR EXERCÍCIO")
        
        nome = ler_texto("Digite o nome para buscar: ")
        resultado = self.exercicio_controller.buscar_por_nome(nome)
        
        if resultado['sucesso'] and resultado['dados']:
            print(f"\n{resultado['mensagem']}:\n")
            for exercicio in resultado['dados']:
                print(formatar_exercicio(exercicio))
        else:
            exibir_mensagem("Nenhum exercício encontrado", "info")
        
        pausar()
    
    def atualizar_exercicio(self):
        """Atualiza um exercício existente"""
        limpar_tela()
        exibir_titulo("ATUALIZAR EXERCÍCIO")
        
        # Lista exercícios primeiro
        resultado = self.exercicio_controller.listar()
        if not resultado['dados']:
            exibir_mensagem("Nenhum exercício cadastrado", "info")
            pausar()
            return
        
        for exercicio in resultado['dados']:
            print(formatar_exercicio(exercicio))
        
        print()
        id_exercicio = ler_inteiro("ID do exercício a atualizar: ", minimo=1)
        
        print("\nDeixe em branco para manter o valor atual")
        nome = ler_texto("Novo nome (ou Enter para manter): ", obrigatorio=False)
        tipo = ler_texto("Novo tipo (ou Enter para manter): ", obrigatorio=False)
        
        repeticoes_str = input("Novas repetições (ou Enter para manter): ").strip()
        repeticoes = int(repeticoes_str) if repeticoes_str else None
        
        resultado = self.exercicio_controller.atualizar(
            id_exercicio,
            nome if nome else None,
            tipo if tipo else None,
            repeticoes
        )
        
        if resultado['sucesso']:
            exibir_mensagem(resultado['mensagem'], "sucesso")
            print(formatar_exercicio(resultado['dados']))
        else:
            exibir_mensagem(resultado['mensagem'], "erro")
        
        pausar()
    
    def remover_exercicio(self):
        """Remove um exercício"""
        limpar_tela()
        exibir_titulo("REMOVER EXERCÍCIO")
        
        # Lista exercícios primeiro
        resultado = self.exercicio_controller.listar()
        if not resultado['dados']:
            exibir_mensagem("Nenhum exercício cadastrado", "info")
            pausar()
            return
        
        for exercicio in resultado['dados']:
            print(formatar_exercicio(exercicio))
        
        print()
        id_exercicio = ler_inteiro("ID do exercício a remover: ", minimo=1)
        
        if confirmar("Tem certeza que deseja remover este exercício?"):
            resultado = self.exercicio_controller.deletar(id_exercicio)
            
            if resultado['sucesso']:
                exibir_mensagem(resultado['mensagem'], "sucesso")
            else:
                exibir_mensagem(resultado['mensagem'], "erro")
        else:
            exibir_mensagem("Operação cancelada", "info")
        
        pausar()
    
    def menu_treinos(self):
        """Menu de gerenciamento de treinos"""
        while True:
            limpar_tela()
            exibir_titulo("GERENCIAR TREINOS")
            print("1. Criar Treino")
            print("2. Listar Treinos")
            print("3. Buscar Treino por Nome")
            print("4. Atualizar Treino")
            print("5. Remover Treino")
            print("6. Adicionar Exercício ao Treino")
            print("7. Remover Exercício do Treino")
            print("0. Voltar")
            
            opcao = ler_inteiro("\nEscolha uma opção: ", 0, 7)
            
            if opcao == 1:
                self.criar_treino()
            elif opcao == 2:
                self.listar_treinos()
            elif opcao == 3:
                self.buscar_treino()
            elif opcao == 4:
                self.atualizar_treino()
            elif opcao == 5:
                self.remover_treino()
            elif opcao == 6:
                self.adicionar_exercicio_treino()
            elif opcao == 7:
                self.remover_exercicio_treino()
            elif opcao == 0:
                break
    
    def criar_treino(self):
        """Cria um novo treino"""
        limpar_tela()
        exibir_titulo("CRIAR TREINO")
        
        nome = ler_texto("Nome do treino: ")
        descricao = ler_texto("Descrição (opcional): ", obrigatorio=False)
        
        resultado = self.treino_controller.criar(nome, descricao)
        
        if resultado['sucesso']:
            exibir_mensagem(resultado['mensagem'], "sucesso")
            print(formatar_treino(resultado['dados']))
        else:
            exibir_mensagem(resultado['mensagem'], "erro")
        
        pausar()
    
    def listar_treinos(self):
        """Lista todos os treinos"""
        limpar_tela()
        exibir_titulo("LISTA DE TREINOS")
        
        resultado = self.treino_controller.listar()
        
        if resultado['dados']:
            for treino in resultado['dados']:
                print(formatar_treino(treino))
        else:
            exibir_mensagem("Nenhum treino cadastrado", "info")
        
        pausar()
    
    def buscar_treino(self):
        """Busca treinos por nome"""
        limpar_tela()
        exibir_titulo("BUSCAR TREINO")
        
        nome = ler_texto("Digite o nome para buscar: ")
        resultado = self.treino_controller.buscar_por_nome(nome)
        
        if resultado['sucesso'] and resultado['dados']:
            print(f"\n{resultado['mensagem']}:\n")
            for treino in resultado['dados']:
                print(formatar_treino(treino))
        else:
            exibir_mensagem("Nenhum treino encontrado", "info")
        
        pausar()
    
    def atualizar_treino(self):
        """Atualiza um treino existente"""
        limpar_tela()
        exibir_titulo("ATUALIZAR TREINO")
        
        # Lista treinos primeiro
        resultado = self.treino_controller.listar()
        if not resultado['dados']:
            exibir_mensagem("Nenhum treino cadastrado", "info")
            pausar()
            return
        
        for treino in resultado['dados']:
            print(formatar_treino(treino))
        
        print()
        id_treino = ler_inteiro("ID do treino a atualizar: ", minimo=1)
        
        print("\nDeixe em branco para manter o valor atual")
        nome = ler_texto("Novo nome (ou Enter para manter): ", obrigatorio=False)
        descricao = ler_texto("Nova descrição (ou Enter para manter): ", obrigatorio=False)
        
        resultado = self.treino_controller.atualizar(
            id_treino,
            nome if nome else None,
            descricao if descricao else None
        )
        
        if resultado['sucesso']:
            exibir_mensagem(resultado['mensagem'], "sucesso")
            print(formatar_treino(resultado['dados']))
        else:
            exibir_mensagem(resultado['mensagem'], "erro")
        
        pausar()
    
    def remover_treino(self):
        """Remove um treino"""
        limpar_tela()
        exibir_titulo("REMOVER TREINO")
        
        # Lista treinos primeiro
        resultado = self.treino_controller.listar()
        if not resultado['dados']:
            exibir_mensagem("Nenhum treino cadastrado", "info")
            pausar()
            return
        
        for treino in resultado['dados']:
            print(formatar_treino(treino))
        
        print()
        id_treino = ler_inteiro("ID do treino a remover: ", minimo=1)
        
        if confirmar("Tem certeza que deseja remover este treino?"):
            resultado = self.treino_controller.deletar(id_treino)
            
            if resultado['sucesso']:
                exibir_mensagem(resultado['mensagem'], "sucesso")
            else:
                exibir_mensagem(resultado['mensagem'], "erro")
        else:
            exibir_mensagem("Operação cancelada", "info")
        
        pausar()
    
    def adicionar_exercicio_treino(self):
        """Adiciona um exercício a um treino"""
        limpar_tela()
        exibir_titulo("ADICIONAR EXERCÍCIO AO TREINO")
        
        # Lista treinos
        resultado_treinos = self.treino_controller.listar()
        if not resultado_treinos['dados']:
            exibir_mensagem("Nenhum treino cadastrado", "info")
            pausar()
            return
        
        print("TREINOS DISPONÍVEIS:")
        for treino in resultado_treinos['dados']:
            print(formatar_treino(treino))
        
        print()
        id_treino = ler_inteiro("ID do treino: ", minimo=1)
        
        # Lista exercícios
        resultado_exercicios = self.exercicio_controller.listar()
        if not resultado_exercicios['dados']:
            exibir_mensagem("Nenhum exercício cadastrado", "info")
            pausar()
            return
        
        print("\nEXERCÍCIOS DISPONÍVEIS:")
        for exercicio in resultado_exercicios['dados']:
            print(formatar_exercicio(exercicio))
        
        print()
        id_exercicio = ler_inteiro("ID do exercício: ", minimo=1)
        series = ler_inteiro("Número de séries: ", minimo=1)
        repeticoes = ler_inteiro("Número de repetições: ", minimo=1)
        
        resultado = self.treino_controller.adicionar_exercicio(id_treino, id_exercicio, series, repeticoes)
        
        if resultado['sucesso']:
            exibir_mensagem(resultado['mensagem'], "sucesso")
        else:
            exibir_mensagem(resultado['mensagem'], "erro")
        
        pausar()
    
    def remover_exercicio_treino(self):
        """Remove um exercício de um treino"""
        limpar_tela()
        exibir_titulo("REMOVER EXERCÍCIO DO TREINO")
        
        # Lista treinos
        resultado_treinos = self.treino_controller.listar()
        if not resultado_treinos['dados']:
            exibir_mensagem("Nenhum treino cadastrado", "info")
            pausar()
            return
        
        print("TREINOS DISPONÍVEIS:")
        for treino in resultado_treinos['dados']:
            print(formatar_treino(treino))
        
        print()
        id_treino = ler_inteiro("ID do treino: ", minimo=1)
        
        # Mostra exercícios do treino
        resultado_exercicios = self.relatorio_controller.listar_exercicios_treino(id_treino)
        if not resultado_exercicios['sucesso'] or not resultado_exercicios['dados']:
            exibir_mensagem("Este treino não possui exercícios", "info")
            pausar()
            return
        
        print("\nEXERCÍCIOS NO TREINO:")
        for dados in resultado_exercicios['dados']:
            ex = dados['exercicio']
            print(f"ID: {ex.id} | {ex.nome} - {dados['series']}x{dados['repeticoes']}")
        
        print()
        id_exercicio = ler_inteiro("ID do exercício a remover: ", minimo=1)
        
        if confirmar("Tem certeza que deseja remover este exercício do treino?"):
            resultado = self.treino_controller.remover_exercicio(id_treino, id_exercicio)
            
            if resultado['sucesso']:
                exibir_mensagem(resultado['mensagem'], "sucesso")
            else:
                exibir_mensagem(resultado['mensagem'], "erro")
        else:
            exibir_mensagem("Operação cancelada", "info")
        
        pausar()
    
    def menu_relatorios(self):
        """Menu de relatórios"""
        while True:
            limpar_tela()
            exibir_titulo("RELATÓRIOS")
            print("1. Exercícios de um Treino")
            print("2. Volume Total de um Treino")
            print("3. Estatísticas Gerais")
            print("4. Exercícios Mais Usados")
            print("0. Voltar")
            
            opcao = ler_inteiro("\nEscolha uma opção: ", 0, 4)
            
            if opcao == 1:
                self.relatorio_exercicios_treino()
            elif opcao == 2:
                self.relatorio_volume_treino()
            elif opcao == 3:
                self.relatorio_estatisticas()
            elif opcao == 4:
                self.relatorio_exercicios_populares()
            elif opcao == 0:
                break
    
    def relatorio_exercicios_treino(self):
        """Relatório de exercícios de um treino"""
        limpar_tela()
        exibir_titulo("EXERCÍCIOS DO TREINO")
        
        # Lista treinos
        resultado_treinos = self.treino_controller.listar()
        if not resultado_treinos['dados']:
            exibir_mensagem("Nenhum treino cadastrado", "info")
            pausar()
            return
        
        for treino in resultado_treinos['dados']:
            print(formatar_treino(treino))
        
        print()
        id_treino = ler_inteiro("ID do treino: ", minimo=1)
        
        resultado = self.relatorio_controller.listar_exercicios_treino(id_treino)
        
        if resultado['sucesso'] and resultado['dados']:
            print(f"\n{resultado['mensagem']}:\n")
            for dados in resultado['dados']:
                print(formatar_exercicio_treino(dados))
        else:
            exibir_mensagem(resultado['mensagem'] if not resultado['sucesso'] else "Treino sem exercícios", "info")
        
        pausar()
    
    def relatorio_volume_treino(self):
        """Relatório de volume de um treino"""
        limpar_tela()
        exibir_titulo("VOLUME DO TREINO")
        
        # Lista treinos
        resultado_treinos = self.treino_controller.listar()
        if not resultado_treinos['dados']:
            exibir_mensagem("Nenhum treino cadastrado", "info")
            pausar()
            return
        
        for treino in resultado_treinos['dados']:
            print(formatar_treino(treino))
        
        print()
        id_treino = ler_inteiro("ID do treino: ", minimo=1)
        
        resultado = self.relatorio_controller.volume_treino(id_treino)
        
        if resultado['sucesso']:
            print(f"\nVolume total do treino: {resultado['dados']} (séries × repetições)")
        else:
            exibir_mensagem(resultado['mensagem'], "erro")
        
        pausar()
    
    def relatorio_estatisticas(self):
        """Relatório de estatísticas gerais"""
        limpar_tela()
        exibir_titulo("ESTATÍSTICAS GERAIS")
        
        resultado = self.relatorio_controller.estatisticas()
        
        if resultado['sucesso']:
            stats = resultado['dados']
            print(f"Total de Exercícios: {stats['total_exercicios']}")
            print(f"Total de Treinos: {stats['total_treinos']}")
            print(f"Média de Exercícios por Treino: {stats['media_exercicios_por_treino']}")
            
            if stats['tipos_exercicios']:
                print("\nExercícios por Tipo:")
                for tipo, quantidade in stats['tipos_exercicios'].items():
                    print(f"  • {tipo}: {quantidade}")
        else:
            exibir_mensagem(resultado['mensagem'], "erro")
        
        pausar()
    
    def relatorio_exercicios_populares(self):
        """Relatório de exercícios mais usados"""
        limpar_tela()
        exibir_titulo("EXERCÍCIOS MAIS USADOS")
        
        resultado = self.relatorio_controller.exercicios_populares()
        
        if resultado['sucesso'] and resultado['dados']:
            print(f"\n{resultado['mensagem']}:\n")
            for i, dados in enumerate(resultado['dados'], 1):
                ex = dados['exercicio']
                uso = dados['uso']
                print(f"{i}. {ex.nome} ({ex.tipo}) - Usado em {uso} treino(s)")
        else:
            exibir_mensagem("Nenhum exercício em uso", "info")
        
        pausar()


def main():
    """Função principal"""
    sistema = SistemaGerenciamentoTreinos()
    sistema.menu_principal()


if __name__ == "__main__":
    main()
