"""
============================================================
 EXERCÍCIO 09 - FUNÇÕES
 (referente à aula09.py)
============================================================

ENUNCIADO:
Crie as seguintes funções e chame todas dentro do
"if __name__ == '__main__':":
  1) eh_primo(numero) -> retorna True se o número for primo.
  2) fatorial(numero) -> calcula o fatorial (ex: 5! = 120).
  3) calcular_imc(peso, altura) -> retorna o IMC.
  4) inverter_texto(texto) -> retorna o texto invertido.
  5) converter_temperatura(celsius, unidade="fahrenheit") -> converte
     Celsius para "fahrenheit" (padrão) ou "kelvin", dependendo
     do parâmetro "unidade".
  6) somar_notas(*notas) -> soma uma quantidade variável de notas.
"""


# TODO 1: verificar se é primo
def eh_primo(numero):
    if numero < 2:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True


# TODO 2: calcular fatorial
def fatorial(numero):
    resultado = 1
    for i in range(2, numero + 1):
        resultado *= i
    return resultado


# TODO 3: calcular IMC
def calcular_imc(peso, altura):
    return peso / (altura ** 2)


# TODO 4: inverter texto
def inverter_texto(texto):
    return texto[::-1]


# TODO 5: converter temperatura com parâmetro padrão
def converter_temperatura(celsius, unidade="fahrenheit"):
    if unidade == "fahrenheit":
        return (celsius * 9 / 5) + 32
    elif unidade == "kelvin":
        return celsius + 273.15
    else:
        return celsius  # unidade desconhecida, retorna o valor original


# TODO 6: somar quantidade variável de notas
def somar_notas(*notas):
    return sum(notas)


if __name__ == "__main__":
    print(f"7 é primo? {eh_primo(7)}")
    print(f"10 é primo? {eh_primo(10)}")

    print(f"Fatorial de 5: {fatorial(5)}")

    print(f"IMC (70kg, 1.75m): {calcular_imc(70, 1.75):.2f}")

    print(f"Inverso de 'Python': {inverter_texto('Python')}")

    print(f"30°C em Fahrenheit: {converter_temperatura(30):.1f}")
    print(f"30°C em Kelvin: {converter_temperatura(30, unidade='kelvin'):.2f}")

    print(f"Soma de notas: {somar_notas(8.5, 7.0, 9.2, 6.8)}")
