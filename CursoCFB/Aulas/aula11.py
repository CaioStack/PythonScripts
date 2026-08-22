# Aula 11 - Condicional IF, ELIF e ELSE

a = 10
b = 5
op = "+"
res = 0

if op == "+":
    res = a + b

elif op == "-":
    res = a - b

elif op == "*":
    res = a * b

elif op == "/":
    res = a / b

else:
    print("Operador inválido")

print(str(a) + op + str(b) + " = " + str(res))

clima = "chuva"
dinheiro = 510
lugar = ""

if clima == "sol" and (dinheiro > 300 and dinheiro < 500):
    lugar = "clube"
else:
    lugar = "cinema"

print("Vou ao " + lugar)

# AND
# V V = V
# V F = F
# F V = F
# F F = F

# OR
# V V = V
# V F = V
# F V = V
# F F = F