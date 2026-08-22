"""
============================================================
 EXERCÍCIO 15 - ARQUIVOS, MÓDULOS E LAMBDA - DESAFIO FINAL
 (referente à aula15.py)
============================================================

ENUNCIADO:
Crie um "mini sistema de cadastro de alunos" que:
  1) Peça quantos alunos serão cadastrados, e para cada um,
     peça o nome e a média, salvando cada linha em um arquivo
     "alunos.txt" no formato "nome,media".
  2) Leia o arquivo de volta, linha por linha, montando uma
     lista de dicionários: [{"nome": ..., "media": ...}, ...]
  3) Use uma list comprehension com filter/lambda (ou condicional
     dentro da comprehension) para gerar a lista de aprovados
     (média >= 7).
  4) Exiba cada aluno com sua situação (Aprovado/Reprovado).
  5) Calcule a média geral da turma usando a função sum() com
     uma comprehension.
  6) Ao final, apague o arquivo "alunos.txt" (era só um exemplo).

Este exercício combina TUDO que vimos até aqui: entrada de dados,
laços, condicionais, funções, arquivos, listas/dicionários e
comprehensions. Você consegue! 🚀
"""

import os

caminho_arquivo = "alunos.txt"

# TODO 1: cadastro de alunos e gravação no arquivo
quantidade_alunos = int(input("Quantos alunos deseja cadastrar? "))

with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
    for i in range(1, quantidade_alunos + 1):
        nome = input(f"\nNome do aluno {i}: ")
        media = float(input(f"Média do aluno {nome}: "))
        arquivo.write(f"{nome},{media}\n")

# TODO 2: ler o arquivo e montar a lista de dicionários
alunos = []
with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        nome, media = linha.strip().split(",")
        alunos.append({"nome": nome, "media": float(media)})

# TODO 3: filtrar aprovados usando list comprehension
aprovados = [aluno for aluno in alunos if aluno["media"] >= 7.0]

# TODO 4: exibir situação de cada aluno
print("\n--- Situação dos alunos ---")
for aluno in alunos:
    situacao = "Aprovado" if aluno["media"] >= 7.0 else "Reprovado"
    print(f"{aluno['nome']} -> Média: {aluno['media']:.2f} -> {situacao}")

# TODO 5: média geral da turma (usando comprehension + sum)
media_geral = sum(aluno["media"] for aluno in alunos) / len(alunos)
print(f"\nMédia geral da turma: {media_geral:.2f}")

# Lista de nomes dos aprovados
nomes_aprovados = [aluno["nome"] for aluno in aprovados]
print(f"Alunos aprovados: {nomes_aprovados}")

# TODO 6: remover o arquivo de exemplo
if os.path.exists(caminho_arquivo):
    os.remove(caminho_arquivo)
    print(f"\nArquivo '{caminho_arquivo}' removido (era só um exemplo).")

"""
------------------------------------------------------------
PARABÉNS por chegar até aqui! 🎉
Continue praticando: crie variações desse sistema, adicione
validações extras, ou tente resolver o mesmo problema usando
bibliotecas externas como Pandas como próximo passo de estudo.
------------------------------------------------------------
"""
