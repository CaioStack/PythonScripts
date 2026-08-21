"""
============================================================
 AULA 10 - DICIONÁRIOS E CONJUNTOS (dict e set)
============================================================

DICIONÁRIO (dict): coleção de pares CHAVE -> VALOR, equivalente
ao HashMap do Java. É muito usado em Python para representar
dados estruturados (parecido com um objeto JSON).

CONJUNTO (set): coleção que NÃO permite valores DUPLICADOS e
não mantém ordem definida. Equivalente ao HashSet do Java.
"""

# ---------------- CRIANDO E USANDO DICIONÁRIOS ----------------
pessoa = {
    "nome": "Lucas",
    "idade": 25,
    "cidade": "Fortaleza"
}

print(f"Nome: {pessoa['nome']}")
print(f"Idade: {pessoa['idade']}")

# Adicionando ou atualizando uma chave
pessoa["profissao"] = "Desenvolvedor"  # adiciona nova chave
pessoa["idade"] = 26                    # atualiza chave existente
print(f"\nDicionário atualizado: {pessoa}")

# get() é mais SEGURO que [] para acessar chaves que podem não existir
print(f"\nTelefone (com get, chave que não existe): {pessoa.get('telefone')}")
print(f"Telefone com valor padrão: {pessoa.get('telefone', 'Não informado')}")

# Verificando se uma chave existe
print(f"Tem a chave 'cidade'? {'cidade' in pessoa}")

# Removendo uma chave
pessoa.pop("cidade")
print(f"\nApós remover 'cidade': {pessoa}")

# ---------------- PERCORRENDO UM DICIONÁRIO ----------------
print("\n--- Percorrendo apenas as chaves ---")
for chave in pessoa.keys():
    print(chave)

print("\n--- Percorrendo apenas os valores ---")
for valor in pessoa.values():
    print(valor)

print("\n--- Percorrendo chave e valor juntos ---")
for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")

# ---------------- DICIONÁRIO DE PREÇOS (exemplo prático) ----------------
precos = {
    "Notebook": 3200.00,
    "Mouse": 79.90,
    "Teclado": 150.00
}

print(f"\nPreço do Notebook: R$ {precos['Notebook']}")
precos["Mouse"] = 69.90  # atualiza o preço
print(f"Novo preço do Mouse: R$ {precos['Mouse']}")

# ---------------- DICT COMPREHENSION ----------------
quadrados_dict = {numero: numero ** 2 for numero in range(1, 6)}
print(f"\nDict comprehension (quadrados): {quadrados_dict}")

# ---------------- CONJUNTOS (set) ----------------
numeros_repetidos = [1, 2, 2, 3, 3, 3, 4, 5, 5]
numeros_unicos = set(numeros_repetidos)  # remove duplicados automaticamente
print(f"\nLista original: {numeros_repetidos}")
print(f"Conjunto (sem duplicados): {numeros_unicos}")

# Criando um set diretamente com chaves { }
frutas_set = {"Maçã", "Banana", "Uva"}
frutas_set.add("Laranja")     # adiciona um elemento
frutas_set.add("Maçã")        # tentar adicionar duplicado não faz nada
print(f"\nConjunto de frutas: {frutas_set}")
print(f"'Banana' está no conjunto? {'Banana' in frutas_set}")

# Operações matemáticas de conjuntos (muito úteis!)
pares = {2, 4, 6, 8, 10}
multiplos_de_3 = {3, 6, 9}

print(f"\nUnião: {pares | multiplos_de_3}")            # todos os elementos
print(f"Interseção: {pares & multiplos_de_3}")          # elementos em comum (6)
print(f"Diferença (pares - mult3): {pares - multiplos_de_3}")  # só em "pares"

"""
------------------------------------------------------------
RESUMO DA AULA
------------------------------------------------------------
- dict: coleção chave -> valor, equivalente ao HashMap do Java
  dicionario[chave], .get(), .keys(), .values(), .items()
- set: coleção sem duplicados, equivalente ao HashSet do Java
  .add(), operadores | (união), & (interseção), - (diferença)
- dict comprehension: {chave: valor for item in sequencia}
============================================================
"""
