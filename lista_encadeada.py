from __future__ import annotations
from typing import Optional
from aluno import Aluno


class _No:
    """Nó interno que armazena o objeto Aluno e o ponteiro para o próximo nó."""
    def __init__(self, aluno: Aluno):
        self.aluno = aluno
        self.proximo: Optional[_No] = None


class ListaEncadeada:
    """Lista encadeada própria para gerenciar elementos do tipo Aluno."""
    def __init__(self):
        self.primeiro: Optional[_No] = None

    def esta_vazia(self) -> bool:
        """Verifica se a lista está vazia."""
        return self.primeiro is None

    def inserir_no_final(self, aluno: Aluno) -> bool:
        """Insere um aluno no final da lista, evitando matrículas duplicadas."""
        if not isinstance(aluno, Aluno):
            raise TypeError("É necessário informar um objeto Aluno.")

        novo_no = _No(aluno)

        if self.esta_vazia():
            self.primeiro = novo_no
            return True

        atual = self.primeiro
        if atual.aluno.matricula == aluno.matricula:
            return False  # Matrícula duplicada

        while atual.proximo is not None:
            if atual.proximo.aluno.matricula == aluno.matricula:
                return False  # Matrícula duplicada
            atual = atual.proximo

        atual.proximo = novo_no
        return True

    def buscar(self, matricula: int) -> Optional[Aluno]:
        """Busca um aluno na lista pela matrícula."""
        atual = self.primeiro
        while atual is not None:
            if atual.aluno.matricula == matricula:
                return atual.aluno
            atual = atual.proximo
        return None

    def remover(self, matricula: int) -> bool:
        """Remove um aluno da lista com base na matrícula, mantendo a ordem."""
        if self.esta_vazia():
            return False

        # Se o elemento a ser removido for o primeiro
        if self.primeiro.aluno.matricula == matricula:
            self.primeiro = self.primeiro.proximo
            return True

        atual = self.primeiro
        while atual.proximo is not None:
            if atual.proximo.aluno.matricula == matricula:
                atual.proximo = atual.proximo.proximo
                return True
            atual = atual.proximo

        return False