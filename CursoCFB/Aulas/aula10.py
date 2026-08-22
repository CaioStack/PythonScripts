# Aula 10 - Comando IF

a = 10
b = 5
op = "*"
res = 0

if op == "+":
    res = a + b
    print("Sim")

if op == "-":
    res = a - b

if op == "*":
    res = a * b

if op == "/":
    res = a / b

print(str(a) + op + str(b) + " = " + str(res))