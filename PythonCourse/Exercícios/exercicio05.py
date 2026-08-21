"""
============================================================
 EXERCÍCIO 05 - ESTRUTURAS CONDICIONAIS
 (referente à aula05.py)
============================================================

ENUNCIADO:
Crie um programa que simule a classificação de um IMC (Índice
de Massa Corporal):
  1) Peça o peso (kg) e a altura (m) do usuário via input().
  2) Calcule o IMC: imc = peso / (altura * altura)
  3) Classifique usando if/elif/else:
       IMC < 18.5             -> "Abaixo do peso"
       18.5 <= IMC < 25       -> "Peso normal"
       25   <= IMC < 30       -> "Sobrepeso"
       IMC >= 30              -> "Obesidade"
  4) Use match/case para exibir o "turno" do dia com base em um
     número digitado pelo usuário
     (1 = Manhã, 2 = Tarde, 3 = Noite, outro = Inválido).
"""

# TODO 1: leia peso e altura
peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

# TODO 2: calcule o IMC
imc = peso / (altura * altura)
print(f"Seu IMC é: {imc:.2f}")

# TODO 3: classifique o IMC
if imc < 18.5:
    classificacao = "Abaixo do peso"
elif imc < 25:
    classificacao = "Peso normal"
elif imc < 30:
    classificacao = "Sobrepeso"
else:
    classificacao = "Obesidade"
print(f"Classificação: {classificacao}")

# TODO 4: match/case para o turno do dia
turno = int(input("Digite um número (1-Manhã, 2-Tarde, 3-Noite): "))

match turno:
    case 1:
        nome_turno = "Manhã"
    case 2:
        nome_turno = "Tarde"
    case 3:
        nome_turno = "Noite"
    case _:
        nome_turno = "Inválido"
print(f"Turno escolhido: {nome_turno}")
