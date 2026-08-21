"""
============================================================
 AULA 03 - OPERADORES
============================================================

Nesta aula veremos os principais grupos de operadores do Python:
  1) Aritméticos      -> +  -  *  /  //  %  **
  2) Atribuição        -> =  +=  -=  *=  /=  %=
  3) Comparação (relacionais) -> ==  !=  >  <  >=  <=
  4) Lógicos           -> and  or  not
"""

# ---------------- OPERADORES ARITMÉTICOS ----------------
a = 10
b = 3

print(f"a + b = {a + b}")   # soma
print(f"a - b = {a - b}")   # subtração
print(f"a * b = {a * b}")   # multiplicação
print(f"a / b = {a / b}")   # divisão: em Python, / SEMPRE retorna float!
print(f"a // b = {a // b}") # divisão INTEIRA (floor division), trunca o decimal
print(f"a % b = {a % b}")   # resto da divisão (módulo)
print(f"a ** b = {a ** b}") # potenciação (a elevado a b) - Python não tem operador ^ para isso!

# IMPORTANTE: diferente do Java, "a / b" com dois inteiros já
# retorna float automaticamente. Não é preciso fazer cast manual.

# ---------------- OPERADORES DE ATRIBUIÇÃO ----------------
contador = 5
contador += 3  # equivale a: contador = contador + 3
print(f"\ncontador += 3 -> {contador}")
contador -= 2
contador *= 2
contador //= 4
print(f"contador após operações -> {contador}")

# IMPORTANTE: Python NÃO tem operadores ++ ou -- (incremento/decremento)!
# Use += 1 ou -= 1 no lugar
x = 5
x += 1  # equivalente ao x++ do Java
print(f"\nx após x += 1 -> {x}")
x -= 1  # equivalente ao x-- do Java
print(f"x após x -= 1 -> {x}")

# ---------------- OPERADORES DE COMPARAÇÃO ----------------
nota1 = 8
nota2 = 6
print(f"\nnota1 == nota2 -> {nota1 == nota2}")
print(f"nota1 != nota2 -> {nota1 != nota2}")
print(f"nota1 > nota2  -> {nota1 > nota2}")
print(f"nota1 < nota2  -> {nota1 < nota2}")
print(f"nota1 >= 8     -> {nota1 >= 8}")

# Python permite ENCADEAR comparações (recurso que o Java não tem!)
idade = 20
print(f"18 <= idade <= 65 -> {18 <= idade <= 65}")  # equivale a (18 <= idade) and (idade <= 65)

# ---------------- OPERADORES LÓGICOS ----------------
# Em Python usamos as PALAVRAS "and", "or" e "not" (não símbolos && || !)
maior_de_idade = True
possui_cnh = False

# and -> só é True se AMBOS forem True
print(f"\nPode dirigir? {maior_de_idade and possui_cnh}")

# or -> é True se PELO MENOS UM for True
print(f"Maior de idade OU possui CNH? {maior_de_idade or possui_cnh}")

# not -> inverte o valor booleano
print(f"NÃO possui CNH? {not possui_cnh}")

# Combinando operadores relacionais e lógicos (muito comum na prática)
saldo_conta = 150.0
pode_comprar = (idade >= 18) and (saldo_conta > 100.0)
print(f"Pode realizar a compra? {pode_comprar}")

# ---------------- OPERADOR "in" (bem comum em Python) ----------------
vogais = "aeiou"
letra = "e"
print(f"\n'{letra}' é vogal? {letra in vogais}")

"""
------------------------------------------------------------
RESUMO DA AULA
------------------------------------------------------------
- "/" sempre retorna float; "//" faz divisão inteira (floor)
- "**" é o operador de potenciação
- Python NÃO tem ++ ou --; use += 1 / -= 1
- Comparações podem ser ENCADEADAS: 18 <= idade <= 65
- Operadores lógicos usam PALAVRAS: and, or, not (não símbolos)
- "in" verifica se um valor existe dentro de outro (string, lista...)
============================================================
"""
