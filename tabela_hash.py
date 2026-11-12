
from typing import List

from aluno import Aluno
from lista_encadeada import ListaEncadeada


class TabelaHash:
    """Tabela hash de alunos com 11 posições e tratamento por lista encadeada."""

    TAMANHO = 11

    def __init__(self):
        self.tabela: List[ListaEncadeada] = [
            ListaEncadeada() for _ in range(self.TAMANHO)
        ]

    def funcao_hash(self, matricula: int) -> int:
        """Calcula a posição da matrícula na tabela."""
        if not isinstance(matricula, int) or isinstance(matricula, bool):
            raise TypeError("A matrícula deve ser um número inteiro.")

        return matricula % self.TAMANHO

    def inserir(self, aluno: Aluno) -> bool:
        """Insere um aluno, impedindo matrículas duplicadas."""
        if not isinstance(aluno, Aluno):
            raise TypeError("É necessário informar um objeto Aluno.")

        indice = self.funcao_hash(aluno.matricula)

        return self.tabela[indice].inserir_no_final(aluno)

    def buscar(self, matricula: int):
        """Busca um aluno pela matrícula."""
        indice = self.funcao_hash(matricula)

        return self.tabela[indice].buscar(matricula)

    def remover(self, matricula: int) -> bool:
        """Remove um aluno pela matrícula."""
        indice = self.funcao_hash(matricula)

        return self.tabela[indice].remover(matricula)
