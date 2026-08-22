# Aula 15 - Tuplas

# As listas são mutáveis, as tuplas são imutáveis

# l_carros = ["HRV", "Golf", "Argo"]
t_carros = ("HRV", "Golf", "Argo")

# Uma forma de "deixar" tuplas mutáveis

t2_carros = list(t_carros) # Convertendo de tupla para lista, assim ficando mutável

t2_carros[2] = "Focus" # Trocando o item 2 "Argo" para "Focus" em formato de lista
t_carros = tuple(t2_carros) # Trocando de volta, de lista para tupla

for x in t_carros:
    print(x)