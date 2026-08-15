"""
============================================================
 AULA 01 - INTRODUÇÃO AO PYTHON
============================================================

Bem-vindo(a) ao curso de Python! Nesta primeira aula você vai
aprender:
  1) O que é Python e como um script Python é organizado
  2) Como exibir mensagens no console
  3) Como escrever comentários
  4) Diferenças importantes em relação ao Java

------------------------------------------------------------
SOBRE A LINGUAGEM
------------------------------------------------------------
Python é uma linguagem INTERPRETADA (não precisa ser compilada
antes de rodar) e DINAMICAMENTE TIPADA (uma variável pode
"trocar de tipo" livremente, diferente do Java).

Diferente do Java, em Python:
  - NÃO existe uma classe obrigatória nem um método "main"
  - Os blocos de código são definidos por INDENTAÇÃO (espaços),
    e não por chaves { }
  - Não é obrigatório usar ponto e vírgula ";" ao final das linhas

------------------------------------------------------------
TIPOS DE COMENTÁRIOS EM PYTHON
------------------------------------------------------------
# Comentário de uma linha

'''
Comentário de várias linhas (na prática é uma string que não
é atribuída a nada, então o Python apenas a ignora)
'''

Este bloco de texto entre aspas triplas no TOPO do arquivo,
como o que você está lendo agora, é chamado de DOCSTRING do
módulo. É a primeira instrução do arquivo e serve para
documentar o que o script faz.
"""

# print() é a função usada para exibir mensagens no console
print("Olá, mundo!")

# Por padrão, print() pula uma linha ao final (equivalente ao
# System.out.println() do Java)
print("Esta linha", "fica separada", "por espaços (padrão do print)")

# Para NÃO pular linha ao final, usamos o parâmetro "end"
print("Este texto ", end="")
print("fica na mesma linha.")

# f-strings (a partir do Python 3.6) permitem formatar texto
# de forma parecida com o printf() do Java
linguagem = "Python"
ano = 2026
print(f"Estou aprendendo {linguagem} em {ano}.")

# Não existe ";" obrigatório ao final das instruções
print("Fim da Aula 01!")

"""
------------------------------------------------------------
RESUMO DA AULA
------------------------------------------------------------
- Python não precisa de classe nem de "main" para rodar um script
- Blocos de código são definidos por INDENTAÇÃO, não por chaves
- print() exibe mensagens no console
- f"texto {variavel}" é a forma moderna de formatar strings
- Comentários: # para uma linha, ''' ''' ou \"\"\" \"\"\" para várias

Agora vá para o Exercício 01 e pratique o que aprendeu!
============================================================
"""
