"""
============================================================
 EXERCÍCIO 08 - STRINGS E MANIPULAÇÃO DE TEXTO
 (referente à aula08.py)
============================================================

ENUNCIADO:
1) Peça ao usuário um e-mail. Verifique se ele CONTÉM o
   caractere "@" e se termina com ".com". Exiba se o e-mail
   "parece válido" ou não.
2) Peça uma frase e conte quantas vezes a palavra "python"
   aparece (ignorando maiúsculas/minúsculas).
3) Peça o nome completo do usuário e exiba somente o
   PRIMEIRO NOME (dica: use split(" ") e pegue a posição 0).
4) Crie um verificador de PALÍNDROMO: uma palavra é palíndromo
   quando é igual de trás para frente (ex.: "arara", "ovo").
   Use fatiamento [::-1] para inverter a palavra e comparar
   com a original.
"""

# TODO 1: validação simples de e-mail
email = input("Digite um e-mail: ")
parece_valido = "@" in email and email.lower().endswith(".com")
print(f"E-mail parece válido? {parece_valido}")

# TODO 2: contar ocorrências da palavra "python"
frase = input("\nDigite uma frase: ")
palavras = frase.split(" ")
contador = 0
for palavra in palavras:
    if palavra.lower() == "python":
        contador += 1
print(f"A palavra 'python' apareceu {contador} vez(es).")

# TODO 3: extrair o primeiro nome
nome_completo = input("\nDigite seu nome completo: ")
primeiro_nome = nome_completo.split(" ")[0]
print(f"Seu primeiro nome é: {primeiro_nome}")

# TODO 4: verificador de palíndromo
palavra = input("\nDigite uma palavra para verificar se é palíndromo: ").lower().strip()
invertida = palavra[::-1]
eh_palindromo = palavra == invertida
print(f"'{palavra}' é palíndromo? {eh_palindromo}")
