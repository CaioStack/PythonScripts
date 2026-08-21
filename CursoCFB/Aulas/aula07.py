# Aula 07 - Strings P2

curso = " Curso de Python "

# print(curso[10:16]) # Python
# print("Tamanho: " + str(len(curso))) # Tamanho: 17, pq len começa a conta em 1
# print(curso.strip()) # Remove os espaços em branco do início e do fim da string
# print(curso.lower().strip()) # Converte a string para minúsculo e tira os espaços
# print(curso.upper().strip()) # Converte a string para maiúsculo e tira os espaços
# print(curso.replace("Python", "Java").strip()) # Substitui a palavra Python por Java e tira os espaços
# a = curso.split(" ") # Divide a string em uma lista de palavras, usando o espaço como separador
# print(a[1]) # Imprime a segunda palavra da lista após ser dividida, que é "Curso"

res = "Python" in curso # Verifica se a palavra "Python" está contida na string curso
print(res) # True, pois "Python" está contido na string curso

res2 = "Python" not in curso # Verifica se a palavra "Python" não está contida na string curso
print(res2) # False, pois "Python" está contido na string curso

texto = "Curso de Python"
palavra = "python"

res = palavra.upper() in texto.upper() # Verifica se a palavra "python" (convertida para maiúsculo) está contida na string texto (também convertida para maiúsculo)
print(res) # True, pois "PYTHON" está contido na string "CURSO DE PYTHON"

canal = "CFB Cursos"
res3 = curso + " do canal " + canal # Concatena as duas strings curso e canal
print(res3) # Imprime a string concatenada " Curso de Python do canal CFB Cursos"

dia = 15
mes = "Dezembro"
ano = 2019
cidade = "Belo Horizonte"

print(cidade + ", " + str(dia) + " de " + mes + " de " + str(ano)) # Imprime a data formatada com a cidade, dia, mês e ano

data = "{}, {} de {} de {}".format(cidade, dia, mes, ano, canal) # Formata a string usando o método format
print(data) # Imprime a data formatada com a cidade, dia, mês e ano

# \n - Quebra de linha
# \t - Tabulação
# \' - Apóstrofo
# \" - Aspas duplas
# \b - Backspace