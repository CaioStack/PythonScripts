# Aula 06 - Strings P1

curso = " Curso de Python "

print(curso[10:16]) # Python

print("Tamanho: " + str(len(curso))) # Tamanho: 17, pq len começa a conta em 1

print(curso.strip()) # Remove os espaços em branco do início e do fim da string

print(curso.lower().strip()) # Converte a string para minúsculo e tira os espaços

print(curso.upper().strip()) # Converte a string para maiúsculo e tira os espaços

print(curso.replace("Python", "Java").strip()) # Substitui a palavra Python por Java e tira os espaços

a = curso.split(" ") # Divide a string em uma lista de palavras, usando o espaço como separador

print(a[1]) # Imprime a segunda palavra da lista após ser dividida, que é "Curso"