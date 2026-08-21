"""
============================================================
 EXERCÍCIO 07 - LISTAS E TUPLAS
 (referente à aula07.py)
============================================================

ENUNCIADO:
1) Crie uma lista vazia e preencha com 5 notas digitadas pelo
   usuário (use input() + append() dentro de um for).
2) Calcule e exiba a MÉDIA das notas da lista.
3) Exiba a MAIOR e a MENOR nota da lista (dica: use max() e min()).
4) Crie uma list comprehension que gere uma nova lista contendo
   apenas as notas >= 7 (aprovadas).
5) Crie uma tupla com as coordenadas (x, y) de um ponto e
   desempacote-a em duas variáveis separadas.
"""

# TODO 1: preencher lista de notas
notas = []
for i in range(1, 6):
    nota = float(input(f"Digite a nota {i}: "))
    notas.append(nota)

print(f"\nNotas digitadas: {notas}")

# TODO 2: calcular a média
media = sum(notas) / len(notas)
print(f"Média das notas: {media:.2f}")

# TODO 3: maior e menor nota
print(f"Maior nota: {max(notas)}")
print(f"Menor nota: {min(notas)}")

# TODO 4: list comprehension com as notas aprovadas
aprovadas = [nota for nota in notas if nota >= 7]
print(f"Notas aprovadas (>= 7): {aprovadas}")

# TODO 5: tupla de coordenadas
ponto = (15, 30)
x, y = ponto
print(f"\nPonto: {ponto} -> x={x}, y={y}")
