"""
============================================================
 EXERCÍCIO 10 - DICIONÁRIOS E CONJUNTOS
 (referente à aula10.py)
============================================================

ENUNCIADO:
1) Crie um dicionário vazio chamado "produto" e preencha com as
   chaves: nome, preco e quantidade, pedindo os valores ao usuário.
2) Exiba as informações formatadas usando .items().
3) Calcule o valor total em estoque (preco * quantidade) e
   adicione esse valor ao dicionário com a chave "valor_total".
4) Crie dois conjuntos com nomes de alunos de duas turmas
   diferentes e exiba: quais alunos estão em AMBAS as turmas
   (interseção) e quais estão em QUALQUER uma delas (união).
"""

# TODO 1: preencher o dicionário do produto
produto = {}
produto["nome"] = input("Nome do produto: ")
produto["preco"] = float(input("Preço do produto: "))
produto["quantidade"] = int(input("Quantidade em estoque: "))

# TODO 2: exibir informações formatadas
print("\n--- Informações do produto ---")
for chave, valor in produto.items():
    print(f"{chave}: {valor}")

# TODO 3: calcular valor total em estoque
produto["valor_total"] = produto["preco"] * produto["quantidade"]
print(f"\nValor total em estoque: R$ {produto['valor_total']:.2f}")

# TODO 4: conjuntos de alunos
turma_a = {"Ana", "Bruno", "Carla", "Diego"}
turma_b = {"Carla", "Diego", "Elisa", "Fábio"}

print(f"\nTurma A: {turma_a}")
print(f"Turma B: {turma_b}")
print(f"Alunos em AMBAS as turmas (interseção): {turma_a & turma_b}")
print(f"Alunos em QUALQUER turma (união): {turma_a | turma_b}")
print(f"Alunos só na Turma A (diferença): {turma_a - turma_b}")
