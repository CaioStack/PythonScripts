"""
============================================================
 AULA 08 - STRINGS E MANIPULAÇÃO DE TEXTO
============================================================

Strings em Python, assim como no Java, são IMUTÁVEIS: qualquer
operação que "altera" uma string, na verdade cria uma NOVA
string na memória.

Uma diferença importante: em Python, uma string pode ser tratada
como uma SEQUÊNCIA de caracteres, permitindo indexação e
fatiamento (slicing), assim como as listas.
"""

frase = "  Aprendendo Python na Prática  "

# ---------------- PROPRIEDADES E MÉTODOS BÁSICOS ----------------
print(f"Tamanho (com espaços): {len(frase)}")
print(f"Maiúsculas: {frase.upper()}")
print(f"Minúsculas: {frase.lower()}")
print(f"Sem espaços nas pontas: [{frase.strip()}]")
print(f"Capitalizado: {frase.strip().capitalize()}")  # só a 1ª letra maiúscula

# ---------------- INDEXAÇÃO E FATIAMENTO (igual às listas!) ----------------
texto = "Python"
print(f"\nPrimeiro caractere: {texto[0]}")
print(f"Último caractere: {texto[-1]}")
print(f"Fatia [1:4]: {texto[1:4]}")
print(f"Texto invertido: {texto[::-1]}")

# ---------------- BUSCANDO DENTRO DA STRING ----------------
texto2 = "Python é uma linguagem interpretada"
print(f"\nContém 'Python'? {'Python' in texto2}")
print(f"Posição da palavra 'linguagem': {texto2.find('linguagem')}")
print(f"Começa com 'Python'? {texto2.startswith('Python')}")
print(f"Termina com 'interpretada'? {texto2.endswith('interpretada')}")

# ---------------- COMPARANDO STRINGS ----------------
s1 = "python"
s2 = "PYTHON"
# Em Python, "==" JÁ compara o CONTEÚDO das strings corretamente
# (diferente do Java, onde "==" compara REFERÊNCIA e não conteúdo)
print(f"\ns1 == s2: {s1 == s2}")                    # False (diferencia maiúsc/minúsc)
print(f"s1.lower() == s2.lower(): {s1.lower() == s2.lower()}")  # True

# ---------------- SUBSTITUINDO E DIVIDINDO ----------------
frase_palavras = "Python,Java,C#,JavaScript"
print(f"\nReplace: {frase_palavras.replace(',', ' | ')}")

# split() quebra a string em uma LISTA, usando um separador
linguagens = frase_palavras.split(",")
print("--- Linguagens separadas ---")
for linguagem in linguagens:
    print(f"- {linguagem}")

# join() faz o INVERSO do split(): junta uma lista em uma única string
linguagens_juntas = " | ".join(linguagens)
print(f"\nJoin: {linguagens_juntas}")

# ---------------- CONCATENAÇÃO ----------------
nome = "Ana"
sobrenome = "Souza"
# Forma 1: operador +
nome_completo1 = nome + " " + sobrenome
# Forma 2: f-string (mais moderna e legível)
nome_completo2 = f"{nome} {sobrenome}"
print(f"\nConcatenado (+): {nome_completo1}")
print(f"Concatenado (f-string): {nome_completo2}")

# ---------------- FORMATAÇÃO NUMÉRICA COM F-STRING ----------------
valor = 1234.5678
print(f"\nCom 2 casas decimais: {valor:.2f}")
print(f"Com separador de milhar: {valor:,.2f}")
print(f"Como porcentagem: {0.256:.1%}")

# ---------------- VERIFICANDO CONTEÚDO ----------------
vazia = ""
com_espacos = "   "
print(f"\nString vazia? {vazia == ''}")
print(f"Só espaços em branco? {com_espacos.isspace()}")
print(f"'123' é numérico? {'123'.isdigit()}")
print(f"'abc' é alfabético? {'abc'.isalpha()}")

"""
------------------------------------------------------------
RESUMO DA AULA
------------------------------------------------------------
- Strings são imutáveis, assim como no Java
- Strings podem ser indexadas e fatiadas como listas: texto[0], texto[1:4]
- "==" já compara CONTEÚDO corretamente (diferente do Java)
- split() quebra a string em lista; join() faz o inverso
- f-strings permitem formatação avançada: f"{valor:.2f}"
- isdigit(), isalpha(), isspace() ajudam a validar conteúdo
============================================================
"""
