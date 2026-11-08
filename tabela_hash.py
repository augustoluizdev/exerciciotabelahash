from __future__ import annotations

from typing import List, Optional

from aluno import Aluno


class _No:
    def __init__(self, aluno: Aluno):
        self.aluno = aluno
        self.proximo: Optional[_No] = None


class TabelaHash:
    def __init__(self):
        self.tabela: List[Optional[_No]] = [None] * 11

    def inserir(self, aluno: Aluno) -> bool:
        if not isinstance(aluno, Aluno):
            raise TypeError("É necessário informar um objeto Aluno.")

        indice = aluno.matricula % 11
        atual = self.tabela[indice]
        novo_no = _No(aluno)

        if atual is None:
            self.tabela[indice] = novo_no
            return True

        while True:
            if atual.aluno.matricula == aluno.matricula:
                return False

            if atual.proximo is None:
                atual.proximo = novo_no
                return True

            atual = atual.proximo