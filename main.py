from aluno import Aluno
from tabela_hash import TabelaHash


def ler_inteiro(mensagem: str) -> int:
    while True:
        entrada = input(mensagem).strip()
        try:
            valor = int(entrada)
            return valor
        except ValueError:
            print("Erro: Digite um número inteiro válido.")


def menu_inserir(tabela: TabelaHash) -> None:
    print("\n--- Inserir Aluno ---")
    matricula = ler_inteiro("Digite a matrícula: ")
    nome = input("Digite o nome: ").strip()
    while not nome:
        print("Erro: O nome não pode ser vazio.")
        nome = input("Digite o nome: ").strip()
    idade = ler_inteiro("Digite a idade: ")

    try:
        aluno = Aluno(matricula, nome, idade)
        if tabela.inserir(aluno):
            print(f"Sucesso: Aluno '{nome}' inserido com sucesso na posição {tabela.funcao_hash(matricula)}!")
        else:
            print(f"Erro: Já existe um aluno cadastrado com a matrícula {matricula} (duplicata não permitida).")
    except Exception as e:
        print(f"Erro ao inserir aluno: {e}")


def menu_buscar(tabela: TabelaHash) -> None:
    print("\n--- Buscar Aluno ---")
    matricula = ler_inteiro("Digite a matrícula a buscar: ")
    aluno = tabela.buscar(matricula)
    if aluno:
        print(f"Aluno encontrado na posição {tabela.funcao_hash(matricula)}:")
        print(f"  {aluno}")
    else:
        print(f"Nenhum aluno encontrado com a matrícula {matricula}.")


def menu_remover(tabela: TabelaHash) -> None:
    print("\n--- Remover Aluno ---")
    matricula = ler_inteiro("Digite a matrícula do aluno a remover: ")
    posicao = tabela.funcao_hash(matricula)
    if tabela.remover(matricula):
        print(f"Sucesso: Aluno com matrícula {matricula} removido da posição {posicao}!")
    else:
        print(f"Erro: Não foi encontrado nenhum aluno com a matrícula {matricula} para remoção.")


def menu_exibir(tabela: TabelaHash) -> None:
    print("\n--- Visualização da Tabela Hash ---")
    tabela.exibir()


def main():
    tabela = TabelaHash()

    opcoes = {
        "1": ("Inserir aluno", menu_inserir),
        "2": ("Buscar aluno", menu_buscar),
        "3": ("Remover aluno", menu_remover),
        "4": ("Exibir tabela hash (11 posições)", menu_exibir),
        "5": ("Sair", None),
    }

    while True:
        print("\n===============================")
        print(" GERENCIAMENTO DE ALUNOS (HASH)")
        print("===============================")
        for chave, (descricao, _) in opcoes.items():
            print(f"[{chave}] {descricao}")
        print("-------------------------------")

        opcao = input("Escolha uma opção (1-5): ").strip()

        if opcao == "5":
            print("\nEncerrando o programa. Até logo!")
            break

        if opcao in opcoes and opcoes[opcao][1] is not None:
            opcoes[opcao][1](tabela)
        else:
            print("Opção inválida! Por favor, escolha um número de 1 a 5.")


if __name__ == "__main__":
    main()

