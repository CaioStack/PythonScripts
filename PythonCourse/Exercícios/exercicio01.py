"""
============================================================
 EXERCÍCIO 01 - INTRODUÇÃO AO PYTHON
 (referente à aula01.py)
============================================================

ENUNCIADO:
1) Exiba seu nome completo no console usando print().
2) Em seguida, na MESMA linha, exiba seu curso e a linguagem
   que está estudando, usando dois print() com end="".
3) Utilize uma f-string para exibir uma frase contendo:
   - o ano atual (número inteiro)
   - o nome da linguagem (texto)
   dentro da mesma frase formatada.
4) Adicione comentários explicando o que cada linha faz.

DICA: revise a aula01.py antes de começar.
"""

# TODO 1: exiba seu nome completo aqui
print("Digite seu nome aqui")

# TODO 2: exiba curso + linguagem na mesma linha (use end="" duas vezes)
print("Curso: ", end="")
print("Análise e Desenvolvimento de Sistemas", end="")
print()  # pula linha ao final

# TODO 3: use f-string para exibir ano + linguagem formatados
ano = 2026
linguagem = "Python"
print(f"No ano de {ano} estou estudando {linguagem}.")

"""
------------------------------------------------------------
GABARITO / SOLUÇÃO SUGERIDA (só olhe depois de tentar sozinho!)
------------------------------------------------------------

print("Maria da Silva")

print("Curso: Análise e Desenvolvimento de Sistemas | ", end="")
print("Linguagem: Python", end="")
print()

ano = 2026
linguagem = "Python"
print(f"No ano de {ano} estou estudando {linguagem}.")
"""
