"""
============================================================
 AULA 07 - LISTAS E TUPLAS
============================================================

Diferente do Java, Python NÃO tem arrays de tamanho fixo como
tipo básico da linguagem. No lugar, usamos:

  LISTA (list) -> coleção MUTÁVEL (pode mudar de tamanho e
                   valores), equivalente ao ArrayList do Java
  TUPLA (tuple) -> coleção IMUTÁVEL (não pode mudar depois de
                    criada), usada para dados fixos
"""

# ---------------- CRIANDO LISTAS ----------------
numeros = [10, 20, 30, 40, 50]         # lista de inteiros
frutas = ["Maçã", "Banana", "Uva", "Laranja"]  # lista de strings
mista = [1, "texto", 3.14, True]        # listas podem misturar tipos!

# ---------------- ACESSANDO E ALTERANDO POSIÇÕES ----------------
# O ÍNDICE sempre começa em 0! O último índice é (tamanho - 1)
print(f"Primeira fruta: {frutas[0]}")
print(f"Terceiro número: {numeros[2]}")

# ÍNDICES NEGATIVOS (recurso exclusivo do Python!): -1 é o último elemento
print(f"Última fruta: {frutas[-1]}")
print(f"Penúltima fruta: {frutas[-2]}")

# Alterando um valor (listas são MUTÁVEIS)
numeros[0] = 100
print(f"\nLista após alteração: {numeros}")

# len() -> retorna o TAMANHO da lista (equivale ao .length do Java)
print(f"Quantidade de frutas: {len(frutas)}")

# ---------------- MÉTODOS DE LISTA MAIS USADOS ----------------
numeros.append(60)          # adiciona um elemento ao FINAL
print(f"\nApós append(60): {numeros}")

numeros.insert(0, 5)        # insere na POSIÇÃO especificada
print(f"Após insert(0, 5): {numeros}")

numeros.remove(100)         # remove pelo VALOR (a primeira ocorrência)
print(f"Após remove(100): {numeros}")

ultimo = numeros.pop()      # remove e RETORNA o último elemento
print(f"Removido com pop(): {ultimo} | Lista agora: {numeros}")

numeros.sort()              # ordena a lista em ordem crescente (altera a lista original)
print(f"Após sort(): {numeros}")

numeros.reverse()           # inverte a ordem da lista
print(f"Após reverse(): {numeros}")

print(f"'30' está na lista? {30 in numeros}")

# ---------------- FATIAMENTO (SLICING) - recurso exclusivo do Python ----------------
# lista[inicio:fim] -> pega do índice "inicio" até "fim - 1"
letras = ["a", "b", "c", "d", "e", "f"]
print(f"\nLista completa: {letras}")
print(f"letras[1:4]: {letras[1:4]}")   # ['b', 'c', 'd']
print(f"letras[:3]: {letras[:3]}")     # do início até o índice 2
print(f"letras[3:]: {letras[3:]}")     # do índice 3 até o final
print(f"letras[::2]: {letras[::2]}")   # pula de 2 em 2
print(f"letras[::-1]: {letras[::-1]}") # inverte a lista

# ---------------- PERCORRENDO UMA LISTA ----------------
print("\n--- Percorrendo com for ---")
for fruta in frutas:
    print(f"Fruta: {fruta}")

# Quando precisamos do ÍNDICE junto com o valor, usamos enumerate()
print("\n--- Percorrendo com enumerate() (índice + valor) ---")
for indice, fruta in enumerate(frutas):
    print(f"[{indice}] {fruta}")

# ---------------- LIST COMPREHENSION (recurso muito usado em Python!) ----------------
# Forma resumida de criar listas a partir de outra sequência
quadrados = [numero ** 2 for numero in range(1, 6)]
print(f"\nQuadrados (list comprehension): {quadrados}")

pares = [numero for numero in range(1, 21) if numero % 2 == 0]
print(f"Números pares de 1 a 20: {pares}")

# ---------------- TUPLAS (imutáveis) ----------------
coordenada = (10, 20)  # tupla criada com parênteses
print(f"\nCoordenada: {coordenada}")
print(f"x = {coordenada[0]}, y = {coordenada[1]}")

# coordenada[0] = 99  # <- ERRO! Tuplas NÃO podem ser alteradas

# Tuplas são úteis para retornar múltiplos valores e "desempacotar"
x, y = coordenada
print(f"Desempacotado: x={x}, y={y}")

# ---------------- MATRIZ (lista de listas) ----------------
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("\n--- Percorrendo uma matriz 3x3 ---")
for linha in matriz:
    for valor in linha:
        print(valor, end=" ")
    print()

"""
------------------------------------------------------------
RESUMO DA AULA
------------------------------------------------------------
- list: coleção MUTÁVEL (equivalente ao ArrayList do Java)
- tuple: coleção IMUTÁVEL, criada com parênteses ( )
- Índices começam em 0; índices NEGATIVOS acessam do final
- len(lista) retorna o tamanho
- append, insert, remove, pop, sort, reverse são muito usados
- fatiamento: lista[inicio:fim:passo]
- enumerate() dá acesso a índice + valor ao percorrer
- list comprehension: [expressao for item in sequencia if condicao]
============================================================
"""
