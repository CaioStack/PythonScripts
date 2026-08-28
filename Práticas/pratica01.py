# Conteúdos abordados nesse arquivo de pratica01.py: Variáveis

# Questão 1:
# Crie três variáveis para armazenar seu nome, sua idade e sua altura. Em seguida, exiba os três valores utilizando print().

nome = "Caio Salgado Marques"
idade = 17
altura = 1.69

print("Nome: " + nome, "Idade: " + str(idade), "Altura: " + str(altura))

# Questão 2:
# Crie duas variáveis numéricas, a e b, e troque os valores entre elas (sem criar uma terceira variável). Exiba os valores antes e depois da troca.
a, b = 10, 20
print(a,b)

b, a = b, a
print(b, a)

# Questão 3:
# Crie uma variável x com o valor 10. Sem apagar a variável, faça x receber x + 5 e exiba o novo valor.

x = 10
x += 5

print(x)