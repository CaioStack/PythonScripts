"""
============================================================
 AULA 05 - ESTRUTURAS CONDICIONAIS (if / elif / else)
============================================================

Estruturas condicionais permitem que o programa tome decisões
e execute caminhos diferentes de código dependendo de uma
condição booleana (True ou False).

DIFERENÇA IMPORTANTE EM RELAÇÃO AO JAVA:
Python NÃO usa chaves { } para delimitar blocos de código.
Em vez disso, usa INDENTAÇÃO (espaços no início da linha).
Todas as linhas de um mesmo bloco precisam ter a MESMA indentação
(o padrão recomendado é 4 espaços).
"""

# ---------------- IF SIMPLES ----------------
idade = 20
if idade >= 18:
    print("Você é maior de idade.")  # esta linha está DENTRO do if (indentada)

# ---------------- IF / ELSE ----------------
nota = 5
if nota >= 7:
    print("Aprovado!")
else:
    print("Reprovado!")

# ---------------- IF / ELIF / ELSE (várias condições) ----------------
# Em Python usamos "elif" em vez de "else if"
nota_final = 8
if nota_final >= 9:
    print("Conceito: A")
elif nota_final >= 7:
    print("Conceito: B")
elif nota_final >= 5:
    print("Conceito: C")
else:
    print("Conceito: D")

# ---------------- IF ANINHADO (dentro de outro if) ----------------
tem_carteira = True
idade_motorista = 19
if idade_motorista >= 18:
    if tem_carteira:
        print("Pode dirigir.")
    else:
        print("Precisa tirar a carteira primeiro.")
else:
    print("Ainda não tem idade para dirigir.")

# ---------------- OPERADOR TERNÁRIO (condicional em uma linha) ----------------
# Sintaxe: valor_se_verdadeiro if condicao else valor_se_falso
numero = 7
paridade = "par" if numero % 2 == 0 else "ímpar"
print(f"O número {numero} é {paridade}")

# ---------------- Python NÃO TEM "switch" (até a versão 3.9) ----------------
# A partir do Python 3.10, existe o "match/case", equivalente ao switch:
dia_da_semana = 3
match dia_da_semana:
    case 1:
        nome_dia = "Domingo"
    case 2:
        nome_dia = "Segunda-feira"
    case 3:
        nome_dia = "Terça-feira"
    case 4:
        nome_dia = "Quarta-feira"
    case 5:
        nome_dia = "Quinta-feira"
    case 6:
        nome_dia = "Sexta-feira"
    case 7:
        nome_dia = "Sábado"
    case _:  # "_" funciona como o "default" do switch em Java
        nome_dia = "Dia inválido"
print(f"Dia da semana: {nome_dia}")

# match/case também aceita múltiplos valores no mesmo case, como o switch moderno do Java
mes = 8
match mes:
    case 12 | 1 | 2:
        estacao = "Verão"
    case 3 | 4 | 5:
        estacao = "Outono"
    case 6 | 7 | 8:
        estacao = "Inverno"
    case 9 | 10 | 11:
        estacao = "Primavera"
    case _:
        estacao = "Mês inválido"
print(f"Estação do ano (hemisfério sul): {estacao}")

"""
------------------------------------------------------------
RESUMO DA AULA
------------------------------------------------------------
- Blocos de código são definidos por INDENTAÇÃO, não por { }
- if / elif / else executa código baseado em condições
- operador ternário: valor_se_true if condicao else valor_se_false
- match/case (Python 3.10+) é equivalente ao switch do Java
- "_" no match/case funciona como o "default"
============================================================
"""
