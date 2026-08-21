# Aula 09 - Coleção List/Array

carros = ["HRV", "Golf", "Argo", "Focus"] # Cria uma lista de carros

print(carros) # Imprime a lista completa de carros
print(carros[0]) # Imprime o primeiro carro da lista, que é "HRV"

# carros[3] = "Fusion" # Altera o quarto carro da lista para "Fusion"
# print(carros) # Imprime a lista atualizada de carros

carros.append("Fit") # Adiciona o carro "Fit" ao final da lista
carros.append("Fusion") # Adiciona o carro "Fusion" ao final da lista
carros.append("Polo") # Adiciona o carro "Polo" ao final da lista

carros.remove("Fusion") # Remove o carro "Fusion" da lista
carros.pop() # Remove o último item da lista
del carros[2] # Remove o índice 2 "Argo"

# carros2 = list(carros) # Copia os itens da lista carros para carros2

carros2 = ["Fusca", "147", "Brasilia", "Celta"]

carros3 = carros + carros2 # Junta as duas listas

print(str(len(carros)) + " carros na lista") # Imprime o tamanho da lista
print(str(len(carros3)) + " carros na lista") # Imprime o tamanho da lista carros3

print(carros) # Imprime a lista atualizada de carros
# print(carros2) # Imprime a lista copiada

carros.clear() # Limpa todos os elementos da lista