# Aula 12 - Loop FOR

carros = ["HRV", "Golf", "Argo", "Focus", "Fit", "Fusion", "Polo"]

"""for x in carros:
    print(x)

    if (x == "Golf"):
        print("VW")"""

for i in carros:
    # print(i)
    if (i == "Fit"):
        break
    print(i)

print("Fim do programa")