"""
============================================================
 EXERCÍCIO 04 - ENTRADA DE DADOS (input)
 (referente à aula04.py)
============================================================

ENUNCIADO:
Crie uma "calculadora de média escolar" que:
  1) Peça o nome do aluno (texto).
  2) Peça 3 notas do aluno (números decimais).
  3) Calcule a média aritmética das 3 notas.
  4) Exiba o nome do aluno e a média calculada.
  5) Informe se o aluno foi APROVADO (média >= 7.0) ou
     REPROVADO (média < 7.0).
"""

# TODO 1: leia o nome do aluno
nome_aluno = input("Digite o nome do aluno: ")

# TODO 2: leia as 3 notas (já convertendo para float)
nota1 = float(input("Digite a 1ª nota: "))
nota2 = float(input("Digite a 2ª nota: "))
nota3 = float(input("Digite a 3ª nota: "))

# TODO 3: calcule a média
media = (nota1 + nota2 + nota3) / 3

# TODO 4 e 5: exiba o resultado e a situação do aluno
print(f"\nAluno: {nome_aluno}")
print(f"Média final: {media:.2f}")

if media >= 7.0:
    print("Situação: APROVADO")
else:
    print("Situação: REPROVADO")

"""
------------------------------------------------------------
OBS: A estrutura "if/else" usada acima ainda será vista em
detalhes na Aula 05. Por enquanto, apenas observe o padrão:
ela permite tomar decisões com base em uma condição.
------------------------------------------------------------
"""
