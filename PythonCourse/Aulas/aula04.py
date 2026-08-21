"""
============================================================
 AULA 04 - ENTRADA DE DADOS (input)
============================================================

Até agora todos os valores estavam "fixos" no código. Nesta
aula vamos aprender a LER dados digitados pelo usuário usando
a função input(), que já vem pronta no Python (não precisa
importar nada, diferente do Scanner do Java!).

IMPORTANTE: input() SEMPRE retorna uma string (str), mesmo que
o usuário digite um número. Se quisermos um número de verdade,
precisamos CONVERTER o valor manualmente.
"""

# ---------------- LENDO TEXTO ----------------
nome = input("Digite seu nome: ")  # já retorna uma string, pronta para uso

# ---------------- LENDO NÚMERO INTEIRO ----------------
# input() retorna string, então precisamos converter com int()
idade_texto = input("Digite sua idade: ")
idade = int(idade_texto)

# É comum fazer a leitura e a conversão em uma única linha:
# idade = int(input("Digite sua idade: "))

# ---------------- LENDO NÚMERO DECIMAL ----------------
altura = float(input("Digite sua altura (ex: 1.75): "))

# ---------------- LENDO BOOLEANO (Python não converte automaticamente!) ----------------
# Diferente do Java, não existe um "input_boolean()" pronto.
# Precisamos comparar o texto digitado manualmente:
resposta = input("Você é estudante de TI? (s/n): ")
estudante_ti = resposta.lower() == "s"  # True se digitar "s" ou "S"

# Exibindo tudo que foi lido
print("\n--- Dados recebidos ---")
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Altura: {altura}")
print(f"Estudante de TI: {estudante_ti}")

# NOTA: diferente do Scanner do Java, o input() do Python NÃO tem
# o problema de "buffer restante" ao misturar leitura de números
# e textos - cada input() sempre lê uma linha inteira digitada.

"""
------------------------------------------------------------
RESUMO DA AULA
------------------------------------------------------------
- input("mensagem") exibe a mensagem e lê o que o usuário digitar
- input() SEMPRE retorna uma string (str)
- Para número inteiro: int(input(...))
- Para número decimal: float(input(...))
- Para boolean: não existe conversão automática, comparar
  manualmente (ex: input(...).lower() == "s")
- Não existe "problema de buffer" como no Scanner do Java
============================================================
"""
