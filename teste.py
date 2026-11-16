from aluno import Aluno
from tabela_hash import TabelaHash


def testar_tudo():
    print("========================================")
    print(" INICIANDO TESTES E INTEGRAÇÃO (teste.py)")
    print("========================================")

    tabela = TabelaHash()

    assert len(tabela.tabela) == 11, "A tabela deve ter 11 posições."
    for pos in range(11):
        assert tabela.tabela[pos].esta_vazia(), f"Posição {pos} deveria iniciar vazia."
    print("[OK] Inicialização das 11 posições verificada.")

    assert tabela.funcao_hash(0) == 0
    assert tabela.funcao_hash(11) == 0
    assert tabela.funcao_hash(22) == 0
    assert tabela.funcao_hash(1) == 1
    assert tabela.funcao_hash(12) == 1
    assert tabela.funcao_hash(10) == 10
    print("[OK] Função hash (matricula % 11) verificada.")

    aluno_a = Aluno(3, "Ana", 19)
    aluno_b = Aluno(14, "Bruno", 21)
    aluno_c = Aluno(25, "Carlos", 23)

    assert tabela.inserir(aluno_a) is True
    assert tabela.inserir(aluno_b) is True
    assert tabela.inserir(aluno_c) is True

    pos3_alunos = list(tabela.tabela[3])
    assert len(pos3_alunos) == 3
    assert pos3_alunos[0].matricula == 3
    assert pos3_alunos[1].matricula == 14
    assert pos3_alunos[2].matricula == 25
    print("[OK] Inserção com colisão e preservação da ordem verificadas.")

    aluno_dup1 = Aluno(14, "Bruno Clone", 25)
    assert tabela.inserir(aluno_dup1) is False, "Não deve permitir matrícula duplicada."
    aluno_dup2 = Aluno(3, "Outra Ana", 30)
    assert tabela.inserir(aluno_dup2) is False, "Não deve permitir matrícula duplicada."
    print("[OK] Prevenção de matrículas duplicadas verificada.")

    aluno_d = Aluno(10, "Daniela", 20)
    aluno_e = Aluno(0, "Eduardo", 22)
    assert tabela.inserir(aluno_d) is True
    assert tabela.inserir(aluno_e) is True

    assert tabela.buscar(3) is aluno_a
    assert tabela.buscar(14) is aluno_b
    assert tabela.buscar(25) is aluno_c
    assert tabela.buscar(10) is aluno_d
    assert tabela.buscar(0) is aluno_e
    assert tabela.buscar(999) is None, "Busca por matrícula inexistente deve retornar None."
    print("[OK] Busca (existente e inexistente) verificada.")

    assert tabela.remover(14) is True
    assert tabela.buscar(14) is None
    assert [a.matricula for a in tabela.tabela[3]] == [3, 25]

    assert tabela.remover(3) is True
    assert tabela.buscar(3) is None
    assert [a.matricula for a in tabela.tabela[3]] == [25]

    assert tabela.remover(25) is True
    assert tabela.buscar(25) is None
    assert tabela.tabela[3].esta_vazia()

    assert tabela.remover(999) is False
    print("[OK] Remoção (início, meio, fim e inexistente) verificada.")

    tabela.inserir(aluno_a)
    tabela.inserir(aluno_b)
    tabela.inserir(aluno_d)
    texto_tabela = str(tabela)

    for i in range(11):
        assert f"Posição [{i:2d}]:" in texto_tabela, f"Exibição deve conter a Posição [{i:2d}]."

    print("[OK] Exibição das 11 posições verificada.")
    print("\nVisualização gerada:")
    print(texto_tabela)

    print("\n========================================")
    print(" TODOS OS TESTES PASSARAM COM SUCESSO! ")
    print("========================================")


if __name__ == "__main__":
    testar_tudo()

