class Aluno:
    def __init__(self, matricula: int, nome: str, idade: int):
        if not isinstance(matricula, int) or isinstance(matricula, bool):
            raise TypeError("A matrícula deve ser um número inteiro.")

        self.matricula = matricula
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return (
            f"Matrícula: {self.matricula} | "
            f"Nome: {self.nome} | "
            f"Idade: {self.idade}"
        )    