# Aula 20 - Funções P2

# valores = [1, 5, 3, 2]

def somar(*num):

    r = 0

    for n in num:
        r += n
    print("Soma: "+ str(r))

somar(5, 7)
somar(12, 8, 3)
somar(1, 2, 6, 9)

def textos(*txt):

    for t in txt:

        print(t)

textos("CFB Cursos", "Python", "Canal", "Curso", "Computador")

def carros (c):
    print("Modelo: " + c)

carros("HRV")

# somar(valores) # Lista valores(lá em cima) dentro da função somar