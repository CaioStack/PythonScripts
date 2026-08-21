"""
============================================================
 AULA 02 - VARIÁVEIS E TIPOS DE DADOS
============================================================

Diferente do Java, em Python NÃO precisamos declarar o tipo
da variável. O Python descobre o tipo automaticamente, baseado
no valor atribuído (isso se chama "tipagem dinâmica").

TIPOS PRIMITIVOS MAIS COMUNS:
  int    -> número inteiro           (ex: 10, -5)
  float  -> número decimal           (ex: 3.14, -0.5)
  str    -> texto (string)           (ex: "Python")
  bool   -> verdadeiro ou falso      (True ou False, com maiúscula!)
  complex -> número complexo         (ex: 2 + 3j) - pouco usado no dia a dia

Não existem "char" nem tipos como "long"/"short"/"double" em
Python: int e float já se ajustam automaticamente ao tamanho
necessário.
"""

# Declarando variáveis (sem precisar informar o tipo!)
idade = 20                     # int
altura = 1.75                  # float
nome = "João"                  # str
estudante = True               # bool

print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Altura: {altura}m")
print(f"É estudante? {estudante}")

# type() mostra o tipo da variável em tempo de execução
print(type(idade))     # <class 'int'>
print(type(altura))    # <class 'float'>
print(type(nome))      # <class 'str'>
print(type(estudante)) # <class 'bool'>

# TIPAGEM DINÂMICA: a mesma variável pode "trocar de tipo"
# (isso NÃO é permitido em Java!)
variavel = 10
print(f"\nvariavel = {variavel} -> tipo: {type(variavel)}")
variavel = "agora sou um texto"
print(f"variavel = {variavel} -> tipo: {type(variavel)}")

# CONSTANTES: Python não tem uma palavra-chave "final" como o Java.
# Por convenção, usamos NOMES EM MAIÚSCULO para indicar que o
# valor NÃO deveria ser alterado (é apenas uma convenção, o
# Python não impede a alteração de verdade).
PI = 3.14159
print(f"\nPI: {PI}")

# ---------------- CONVERSÃO DE TIPOS (casting) ----------------
numero_inteiro = 10
numero_decimal = float(numero_inteiro)  # int -> float
print(f"\nConvertido para float: {numero_decimal}")

valor = 9.99
valor_convertido = int(valor)  # float -> int (trunca a parte decimal, NÃO arredonda)
print(f"Convertido para int (perde decimais): {valor_convertido}")

# Convertendo texto para número e número para texto
texto_numero = "42"
numero_convertido = int(texto_numero)     # str -> int
numero_para_texto = str(100)              # int -> str
print(f"Texto convertido para número: {numero_convertido}")
print(f"Número convertido para texto: '{numero_para_texto}'")

# ---------------- MÚLTIPLA ATRIBUIÇÃO (recurso exclusivo do Python) ----------------
# É possível atribuir várias variáveis em uma única linha
x, y, z = 1, 2, 3
print(f"\nx={x}, y={y}, z={z}")

# Também é possível atribuir o MESMO valor a várias variáveis
a = b = c = 0
print(f"a={a}, b={b}, c={c}")

"""
------------------------------------------------------------
RESUMO DA AULA
------------------------------------------------------------
- Python usa TIPAGEM DINÂMICA: não é preciso declarar o tipo
- Tipos básicos: int, float, str, bool, complex
- type(variavel) mostra o tipo atual da variável
- Por convenção, NOMES_EM_MAIUSCULO indicam constantes
- int(), float(), str() convertem entre tipos
- Python permite múltipla atribuição: x, y, z = 1, 2, 3
============================================================
"""
