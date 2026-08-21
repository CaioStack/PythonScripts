# Aula 08 - Tipo Boolean

aula = True
print(aula) # Imprime o valor booleano True

aula2 = False
print(aula2) # Imprime o valor booleano False

calc = 10 > 5 # Verifica se 10 é maior que 5, o resultado é True
print(calc) # Imprime o valor booleano True

calc2 = 10 < 5 # Verifica se 10 é menor que 5, o resultado é False
print(calc2) # Imprime o valor booleano False

aula3 = "CFB Cursos"
print((bool(aula3))) # Imprime o valor booleano True, pois a string não está vazia

vazio = ""
print((bool(vazio))) # Imprime o valor booleano False, pois a string está vazia

num = 0
print((bool(num))) # Imprime o valor booleano False, pois o número é zero

num2 = 10
print((bool(num2))) # Imprime o valor booleano True, pois o número é diferente de zero