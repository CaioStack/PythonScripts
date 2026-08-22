# Aula 14 - Loop WHILE

# inicialização de variável de controle

i = 0

"""while i < 10:

    print(i)

    i += 1

    if (i >=5 ):
        break

print("Fim do programa")"""

carros = ["HRV", "Golf", "Argo", "Onix", "Focus"]

tam = len(carros)

while i < tam:

    print(carros[i])

    i += 1

print("\nFim do Loop")

carros2 = []
carro = input("Digite o nome do novo carro: ")

while carro != "-1":

    carros2.append(carro)

    carro = input("Digite o nome do novo carro: ")

for x in carros2:
    print(x)