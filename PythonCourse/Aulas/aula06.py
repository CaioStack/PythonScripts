"""
============================================================
 AULA 06 - ESTRUTURAS DE REPETIÇÃO (for, while)
============================================================

Laços de repetição (loops) permitem executar um bloco de
código VÁRIAS VEZES, sem precisar repetir o código manualmente.

DIFERENÇA IMPORTANTE EM RELAÇÃO AO JAVA:
O "for" do Python NÃO funciona como o for(int i=0; i<10; i++)
do Java. Em Python, o for sempre PERCORRE algo iterável (uma
sequência de números, uma lista, um texto, etc). Para simular
o "for numérico" do Java, usamos a função range().

Python também NÃO tem "do-while".
"""

# ---------------- FOR com range() ----------------
# range(inicio, fim, passo) gera números de "inicio" até "fim - 1"
print("--- Laço FOR (1 a 5) ---")
for i in range(1, 6):  # começa em 1, vai até 5 (o 6 NÃO é incluído)
    print(f"Contagem: {i}")

# FOR regressivo (passo negativo)
print("\n--- FOR regressivo ---")
for i in range(5, 0, -1):  # de 5 até 1, decrescendo de 1 em 1
    print(f"Regressiva: {i}")

# FOR pulando de 2 em 2
print("\n--- FOR pulando de 2 em 2 ---")
for i in range(0, 11, 2):  # de 0 até 10, pulando de 2 em 2
    print(f"Par: {i}")

# range() sozinho (só o "fim") começa em 0 por padrão
print("\n--- range(5) (equivale a 0,1,2,3,4) ---")
for i in range(5):
    print(f"i = {i}")

# ---------------- WHILE ----------------
# Igual ao Java: a condição é testada ANTES de cada execução do bloco
print("\n--- Laço WHILE ---")
contador = 1
while contador <= 5:
    print(f"While: {contador}")
    contador += 1  # IMPORTANTE: sem isso, o laço nunca termina (loop infinito)

# ---------------- SIMULANDO O "DO-WHILE" (Python não tem) ----------------
# Executamos o bloco pelo menos uma vez, com um "while True" + "break"
print("\n--- Simulando DO-WHILE ---")
numero = 1
while True:
    print(f"Do-while (simulado): {numero}")
    numero += 1
    if numero > 5:
        break  # sai do laço quando a condição de parada é atingida

# ---------------- BREAK e CONTINUE ----------------
print("\n--- BREAK (interrompe o laço) ---")
for i in range(1, 11):
    if i == 6:
        break  # sai do laço imediatamente quando i chega a 6
    print(f"break -> {i}")

print("\n--- CONTINUE (pula para a próxima iteração) ---")
for i in range(1, 11):
    if i % 2 == 0:
        continue  # pula os números pares, sem executar o resto do bloco
    print(f"continue (só ímpares) -> {i}")

# ---------------- LAÇOS ANINHADOS (loop dentro de loop) ----------------
print("\n--- Laços aninhados: tabuada de 1 a 3 ---")
for i in range(1, 4):
    for j in range(1, 6):
        print(f"{i} x {j} = {i * j}")
    print("------")

# ---------------- FOR percorrendo diretamente uma sequência ----------------
# Isso é o "for-each" do Java, mas é o MODO PADRÃO do for em Python
frutas = ["Maçã", "Banana", "Uva"]
print("\n--- Percorrendo uma lista diretamente ---")
for fruta in frutas:
    print(f"Fruta: {fruta}")

"""
------------------------------------------------------------
RESUMO DA AULA
------------------------------------------------------------
- for percorre algo ITERÁVEL (range, lista, string...)
- range(inicio, fim, passo) gera uma sequência de números
- while: testa a condição ANTES de executar (igual ao Java)
- Python NÃO tem do-while; simulamos com while True + break
- break: interrompe o laço completamente
- continue: pula para a próxima iteração
============================================================
"""
