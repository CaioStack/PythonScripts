"""
============================================================
 AULA 15 - MANIPULAÇÃO DE ARQUIVOS E MÓDULOS
============================================================

Nesta última aula veremos:
  1) Como ler e escrever arquivos de texto
  2) Como organizar código em MÓDULOS (importação)
  3) Um recurso avançado muito usado no dia a dia: comprehensions
     combinadas com dicionários e funções lambda
"""

import os

# ---------------- ESCREVENDO EM UM ARQUIVO ----------------
# open(caminho, modo) abre um arquivo. Modos mais comuns:
#   "w" -> escrita (sobrescreve o arquivo se já existir)
#   "a" -> append (adiciona ao final, sem apagar o que já existe)
#   "r" -> leitura

caminho_arquivo = "alunos.txt"

# "with" garante que o arquivo será FECHADO automaticamente ao
# final do bloco, mesmo se ocorrer um erro (equivale a um
# try/finally implícito - é a forma recomendada em Python)
with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
    arquivo.write("Ana,8.5\n")
    arquivo.write("Bruno,6.0\n")
    arquivo.write("Carla,9.2\n")

print(f"Arquivo '{caminho_arquivo}' criado com sucesso!")

# ---------------- LENDO UM ARQUIVO INTEIRO DE UMA VEZ ----------------
with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()
print(f"\n--- Conteúdo completo do arquivo ---\n{conteudo}")

# ---------------- LENDO UM ARQUIVO LINHA POR LINHA ----------------
print("--- Lendo linha por linha ---")
with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        linha = linha.strip()  # remove o "\n" do final
        nome, nota = linha.split(",")
        print(f"Aluno: {nome} | Nota: {nota}")

# ---------------- ADICIONANDO CONTEÚDO (append) ----------------
with open(caminho_arquivo, "a", encoding="utf-8") as arquivo:
    arquivo.write("Diego,7.8\n")
print("\nLinha adicionada ao arquivo!")

# Limpando o arquivo de exemplo ao final (boa prática em scripts de teste)
if os.path.exists(caminho_arquivo):
    os.remove(caminho_arquivo)
    print(f"Arquivo '{caminho_arquivo}' removido (era só um exemplo).")

# ---------------- MÓDULOS ----------------
# Um módulo é simplesmente OUTRO arquivo .py. Para usar funções de
# outro arquivo, usamos "import". Exemplo (não executado aqui):
#
#   # arquivo utilitarios.py
#   def saudacao(nome):
#       return f"Olá, {nome}!"
#
#   # arquivo principal.py
#   import utilitarios
#   print(utilitarios.saudacao("Ana"))
#
#   # ou importando uma função específica:
#   from utilitarios import saudacao
#   print(saudacao("Ana"))

# Python já vem com MUITOS módulos prontos (biblioteca padrão),
# como o "os" (usado acima), "math", "random", "datetime", etc.
import math
import random

print(f"\nRaiz quadrada de 16: {math.sqrt(16)}")
print(f"Número aleatório entre 1 e 10: {random.randint(1, 10)}")

# ---------------- FUNÇÕES LAMBDA (funções anônimas de uma linha) ----------------
# Equivalente às expressões lambda do Java, mas com sintaxe mais direta
dobrar = lambda x: x * 2
print(f"\nDobro de 5: {dobrar(5)}")

# Muito usadas com map(), filter() e sorted()
numeros = [5, 3, 8, 1, 9, 2]

dobrados = list(map(lambda n: n * 2, numeros))
print(f"Números dobrados (map): {dobrados}")

pares = list(filter(lambda n: n % 2 == 0, numeros))
print(f"Apenas os pares (filter): {pares}")

ordenado_decrescente = sorted(numeros, reverse=True)
print(f"Ordenado decrescente (sorted): {ordenado_decrescente}")

"""
------------------------------------------------------------
RESUMO DA AULA
------------------------------------------------------------
- open(caminho, modo) abre arquivos; "with" fecha automaticamente
- modos: "r" leitura, "w" escrita (sobrescreve), "a" append
- .read() lê tudo; "for linha in arquivo" lê linha por linha
- import módulo / from módulo import funcao para reaproveitar código
- lambda parametro: expressao cria funções anônimas rápidas
- map(), filter() e sorted() são muito usados com lambda

PARABÉNS! Você concluiu a trilha básica-intermediária de Python.
Próximos passos sugeridos: list/dict comprehensions avançadas,
tratamento de dados com Pandas, testes automatizados (pytest),
e um framework como Django ou FastAPI.
============================================================
"""
