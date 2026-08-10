#Aula 05 - Tipos númericos, random e operações de casting

import random

num_i = 10 # int
num_f = 5.2 # float
num_c = 1j # complex

num_r = random.randrange(0, 59) # random range

x = num_r

print("Valor : " + str(x) + " Tipo : " + str(type(x)))

x = [ # list / array (Lista)
    random.randrange(0, 59),
    random.randrange(0, 59),
    random.randrange(0, 59),
    random.randrange(0, 59),
    random.randrange(0, 59),
    random.randrange(0, 59)
]

print("Valor : " + str(x[0]))
print("Valor : " + str(x[1]))
print("Valor : " + str(x[2]))
print("Valor : " + str(x[3]))
print("Valor : " + str(x[4]))
print("Valor : " + str(x[5]))