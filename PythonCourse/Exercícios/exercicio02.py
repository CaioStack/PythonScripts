"""
============================================================
 EXERCÍCIO 02 - VARIÁVEIS E TIPOS DE DADOS
 (referente à aula02.py)
============================================================

ENUNCIADO:
Crie um programa que armazene os dados de um produto de uma loja:
  1) nome do produto        (str)
  2) preço do produto       (float)
  3) quantidade em estoque  (int)
  4) produto está em promoção? (bool)

Depois:
  - Exiba todos os dados formatados no console (use f-strings).
  - Exiba o TIPO de cada uma das variáveis usando type().
  - Calcule e exiba o VALOR TOTAL em estoque (preço * quantidade).
  - Crie uma "constante" (por convenção, MAIÚSCULA) chamada
    TAXA_IMPOSTO = 0.10 (10%) e calcule quanto seria o imposto
    sobre o preço do produto.
"""

# TODO 1: declare as variáveis do produto
nome_produto = "Fone de Ouvido Bluetooth"
preco = 149.90
quantidade_estoque = 35
em_promocao = True

# TODO 2: exiba os dados formatados
print(f"Produto: {nome_produto}")
print(f"Preço: R$ {preco}")
print(f"Estoque: {quantidade_estoque} unidades")
print(f"Em promoção? {em_promocao}")

# TODO 3: exiba os tipos das variáveis
print(f"\nTipo de nome_produto: {type(nome_produto)}")
print(f"Tipo de preco: {type(preco)}")
print(f"Tipo de quantidade_estoque: {type(quantidade_estoque)}")
print(f"Tipo de em_promocao: {type(em_promocao)}")

# TODO 4: calcule o valor total em estoque
valor_total_estoque = preco * quantidade_estoque
print(f"\nValor total em estoque: R$ {valor_total_estoque}")

# TODO 5: crie a constante TAXA_IMPOSTO e calcule o imposto
TAXA_IMPOSTO = 0.10
imposto = preco * TAXA_IMPOSTO
print(f"Imposto sobre o preço: R$ {imposto}")

"""
------------------------------------------------------------
Depois de terminar, tente:
- Trocar os valores das variáveis e ver como a saída muda.
- Usar str(preco) para transformar o preço em texto manualmente.
------------------------------------------------------------
"""
