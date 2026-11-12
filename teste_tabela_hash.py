
from aluno import Aluno
from tabela_hash import TabelaHash

tabela = TabelaHash()

# 1. Testar inserção
aluno1 = Aluno(1001, "Victor", 20)
aluno2 = Aluno(1012, "Joao", 21)
aluno3 = Aluno(1023, "Maria", 22)

assert tabela.inserir(aluno1) is True
assert tabela.inserir(aluno2) is True
assert tabela.inserir(aluno3) is True

print("1. Insercao: OK")

# 2. Testar colisões
assert tabela.funcao_hash(1001) == 0
assert tabela.funcao_hash(1012) == 0
assert tabela.funcao_hash(1023) == 0

print("2. Colisoes: OK")

# 3. Testar matrícula duplicada
aluno_duplicado = Aluno(1001, "Outro Nome", 25)
assert tabela.inserir(aluno_duplicado) is False

print("3. Duplicidade: OK")

# 4. Testar busca
assert tabela.buscar(1001) is aluno1
assert tabela.buscar(1012) is aluno2
assert tabela.buscar(9999) is None

print("4. Busca: OK")

# 5. Testar remoção
assert tabela.remover(1012) is True
assert tabela.buscar(1012) is None

assert tabela.remover(1001) is True
assert tabela.remover(1023) is True

print("5. Remocao: OK")

# 6. Testar remoção de matrícula inexistente
assert tabela.remover(9999) is False

print("6. Remocao inexistente: OK")

print("\nTODOS OS TESTES PASSARAM!")
