# Aula 16 - Matrizes

carros = [
    ["Modelo", "HRV"], 
    ["Fabricante", "Honda"], 
    ["Ano", 2016]
    ]

# print(carros[2][0]) -> # Ano

carros.append(["Cor", "Prata"])
carros[2][1] = 2019

for l, c in carros:
    print(l + " | " + str(c))