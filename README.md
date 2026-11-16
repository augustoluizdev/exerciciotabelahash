# Tabela Hash de Alunos

Este projeto implementa uma tabela hash encadeada para armazenar dados de alunos de uma universidade, utilizando tratamento de colisão por listas encadeadas.

## Objetivo

A aplicação permite:
- inserir alunos com matrícula, nome e idade;
- buscar um aluno pela matrícula;
- remover um aluno da tabela;
- exibir todas as posições da tabela hash;
- impedir matrículas duplicadas;
- usar a função de hash `h(chave) = chave mod 11`.

## Requisitos do projeto

- Python 3.x
- Sistema operacional com terminal/Prompt de Comando
- Nenhuma dependência externa

## Estrutura do projeto

```text
exerciciotabelahash/
├── aluno.py
├── lista_encadeada.py
├── main.py
├── tabela_hash.py
├── teste.py
├── teste_tabela_hash.py
└──  README.md
```

## Como rodar o projeto

### 1. Abra o terminal

No diretório do projeto:

```bash
cd C:\Users\Augusto\Desktop\faculdade\projetotabelahash\exerciciotabelahash
```

### 2. Execute o programa principal

```bash
python main.py
```

No Windows, também é possível usar:

```bash
python .\main.py
```

### 3. Menu disponível

O programa apresenta as seguintes opções:

1. Inserir novo Aluno
2. Buscar Aluno
3. Remover Aluno
4. Exibir Tabela Hash
5. Encerrar Sistema

## Como testar o projeto

Você pode rodar os testes inclusos no repositório:

```bash
python teste.py
```

ou

```bash
python teste_tabela_hash.py
```

Esses testes validam:
- tamanho da tabela (11 posições);
- função hash correta;
- colisões;
- matrículas duplicadas;
- busca por aluno existente e inexistente;
- remoção de primeiro, meio e último elemento;
- exibição da tabela.

## Regras da tabela hash

- A tabela possui 11 posições, índices de 0 a 10.
- Cada posição guarda uma lista encadeada.
- A matrícula deve ser um número inteiro.
- A função hash utilizada é:

```python
indice = matricula % 11
```

- Em caso de colisão, o aluno é inserido no final da lista daquela posição.
- Matrículas duplicadas são rejeitadas.

## Participantes

- Augusto Luiz Lima Dantas
- Marcos Vinícios Mendes de Lima
- Ismar Ferreira de Macêdo Neto
- Victor Manoel da Silva
- Pedro Henrique Matos Leitão de Medeiros

## Observações

- O projeto foi desenvolvido em Python puro.
- Não exige instalação de bibliotecas externas.
- O arquivo `main.py` é a interface principal do sistema.

## Autor

Projeto desenvolvido para a disciplina de estrutura de dados, com implementação de tabela hash encadeada em Python.
