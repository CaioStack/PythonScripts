"""
============================================================
 EXERCÍCIO 03 - OPERADORES
 (referente à aula03.py)
============================================================

ENUNCIADO:
1) Declare dois números inteiros (a e b) e exiba o resultado
   das operações: soma, subtração, multiplicação, divisão,
   divisão inteira, módulo e potenciação.
2) Declare uma variável "salario" (float) e aumente-a em 15%
   usando o operador de atribuição composto (+=).
3) Crie duas variáveis booleanas: "tem_experiencia" e
   "tem_formacao". Verifique se a pessoa é APROVADA em uma vaga
   somente se tiver AMBOS (use and).
4) Verifique se a pessoa é apta para uma ENTREVISTA se tiver
   PELO MENOS UM dos dois requisitos (use or).
5) Use comparação encadeada para verificar se uma nota está
   entre 0 e 10.
"""

# TODO 1: operações aritméticas
a = 17
b = 4
print(f"Soma: {a + b}")
print(f"Subtração: {a - b}")
print(f"Multiplicação: {a * b}")
print(f"Divisão: {a / b}")
print(f"Divisão inteira: {a // b}")
print(f"Módulo: {a % b}")
print(f"Potenciação (a elevado a b): {a ** b}")

# TODO 2: aumento de salário em 15%
salario = 2000.0
salario += salario * 0.15
print(f"\nNovo salário: R$ {salario}")

# TODO 3 e 4: lógica de aprovação/entrevista
tem_experiencia = True
tem_formacao = False

aprovado = tem_experiencia and tem_formacao
apto_para_entrevista = tem_experiencia or tem_formacao

print(f"\nAprovado direto na vaga? {aprovado}")
print(f"Apto para entrevista? {apto_para_entrevista}")

# TODO 5: comparação encadeada
nota = 7.5
nota_valida = 0 <= nota <= 10
print(f"\nA nota {nota} é válida (entre 0 e 10)? {nota_valida}")

"""
------------------------------------------------------------
DESAFIO EXTRA (opcional):
Calcule o troco de uma compra: crie "valor_compra" e
"valor_pago" (float), calcule o troco com (valor_pago - valor_compra)
e exiba usando f-string com 2 casas decimais: f"{troco:.2f}"
------------------------------------------------------------
"""
