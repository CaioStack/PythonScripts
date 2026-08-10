# Aula 04 - Tipos de dados

x = 1 #int
x = "CFB Cursos" #str (String)
x = 15.6 #float
x = False #or True #bool (Boolean)

n1 = 5 ; n2 = 2 ; x = complex(n1, n2) #complex (Complexo)

x = ["Carro", "Moto", "Avião", 1, 58.3, True] #list / array (Lista)

x = ("Carro", "Moto", "Avião", 1, 58.3, True) #tuple (Tupla)

x = range(0,100, 5) #range (Intervalo de números)

x = { # dictionary (Dicionário) dict
    "canal": "CFB Cursos",
    "curso": "Python",
    "nome": "Caio",
}

# x[0] = "Bicicleta" #Alterando o valor do índice 0 da lista

"""
print(x.real) # Imprime a parte real do número complexo
print(x.imag) # Imprime a parte imaginária do número complexo

print("valor de x: " + str(x))
print("tipo de x: " + str(type(x))) """

print(x["canal"]) # Imprime o valor da chave "canal" do dicionário