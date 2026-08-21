"""
============================================================
 EXERCÍCIO 06 - ESTRUTURAS DE REPETIÇÃO
 (referente à aula06.py)
============================================================

ENUNCIADO:
1) Usando FOR (com range), exiba a tabuada completa (1 a 10) de
   um número digitado pelo usuário.
2) Usando WHILE, calcule a soma de todos os números de 1 até
   um valor N digitado pelo usuário.
3) Simule um "menu" com while True + break, que continua
   perguntando ao usuário se ele quer continuar (s/n) e some
   quantas vezes ele digitou "s".
4) Usando FOR + IF, exiba somente os números PRIMOS entre 1 e 50.
"""

# TODO 1: tabuada com FOR
numero = int(input("Digite um número para ver a tabuada: "))
print(f"--- Tabuada do {numero} ---")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

# TODO 2: soma de 1 até N com WHILE
n = int(input("\nDigite um valor N para somar de 1 até N: "))
soma = 0
i = 1
while i <= n:
    soma += i
    i += 1
print(f"Soma de 1 até {n} = {soma}")

# TODO 3: menu simulando do-while
quantas_vezes_sim = 0
while True:
    resposta = input("\nDeseja continuar? (s/n): ")
    if resposta.lower() == "s":
        quantas_vezes_sim += 1
    if resposta.lower() != "s":
        break
print(f"Você digitou 's' {quantas_vezes_sim} vez(es).")

# TODO 4: números primos entre 1 e 50
print("\n--- Números primos entre 1 e 50 ---")
for numero_atual in range(2, 51):
    primo = True
    for divisor in range(2, numero_atual):
        if numero_atual % divisor == 0:
            primo = False
            break  # não precisa continuar testando
    if primo:
        print(numero_atual, end=" ")
print()
