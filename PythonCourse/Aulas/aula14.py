"""
============================================================
 AULA 14 - TRATAMENTO DE EXCEÇÕES
============================================================

EXCEÇÕES são erros que ocorrem DURANTE a execução do programa
(ex.: dividir por zero, acessar índice inexistente de uma lista,
converter texto inválido para número). Se não forem tratadas, a
exceção interrompe o programa.

O Python usa os blocos try / except / else / finally para tratar
esses erros de forma controlada, de forma parecida com o
try/catch/finally do Java.
"""

# ---------------- TRY / EXCEPT BÁSICO ----------------
try:
    resultado = 10 / 0  # isso lança ZeroDivisionError
    print(f"Resultado: {resultado}")  # nunca é executado
except ZeroDivisionError:
    print("Erro: não é possível dividir por zero!")

# ---------------- CAPTURANDO A MENSAGEM DO ERRO ----------------
try:
    resultado = 10 / 0
except ZeroDivisionError as erro:
    print(f"Mensagem original do erro: {erro}")

# ---------------- MÚLTIPLOS EXCEPT ----------------
numeros = [1, 2, 3]
try:
    print(numeros[5])  # índice inexistente!
except IndexError:
    print("Erro: posição da lista não existe.")
except Exception as erro:
    # except genérico: pega qualquer outra exceção não tratada acima
    print(f"Erro inesperado: {erro}")

# ---------------- ELSE E FINALLY ----------------
# "else" executa SOMENTE SE não houve nenhum erro no try
# "finally" SEMPRE executa, tenha dado erro ou não (limpeza de recursos)
try:
    texto = None
    print(len(texto))  # TypeError, pois None não tem "length"
except TypeError:
    print("Erro: tentativa de usar um objeto None de forma inválida.")
else:
    print("Nenhum erro ocorreu (não é executado neste exemplo).")
finally:
    print("Bloco finally executado (sempre roda).")

# ---------------- CONVERSÃO INVÁLIDA (ValueError) ----------------
try:
    numero = int("abc")  # não é um número válido!
    print(numero)
except ValueError:
    print("Erro: texto não pode ser convertido para número.")

# ---------------- LANÇANDO EXCEÇÕES MANUALMENTE (raise) ----------------
def validar_idade(idade):
    if idade < 0:
        # "raise" lança a exceção manualmente
        raise ValueError(f"Idade não pode ser negativa: {idade}")
    print(f"Idade válida: {idade}")


try:
    validar_idade(-5)
except ValueError as erro:
    print(f"Erro de validação: {erro}")


# ---------------- CRIANDO E USANDO UMA EXCEÇÃO PERSONALIZADA ----------------
class SaldoInsuficienteError(Exception):
    """Exceção personalizada para saldo insuficiente."""
    pass


def sacar(saldo, valor_saque):
    if valor_saque > saldo:
        raise SaldoInsuficienteError(
            f"Saldo de R$ {saldo} é insuficiente para sacar R$ {valor_saque}"
        )
    print(f"Saque de R$ {valor_saque} realizado com sucesso.")


try:
    sacar(100.0, 500.0)
except SaldoInsuficienteError as erro:
    print(f"Erro personalizado: {erro}")

print("\nPrograma continua normalmente após tratar os erros!")

"""
------------------------------------------------------------
RESUMO DA AULA
------------------------------------------------------------
- try: bloco onde o erro PODE ocorrer
- except TipoDeErro: trata um erro específico
- except TipoDeErro as variavel: captura a mensagem do erro
- else: executa se NÃO houve erro no try
- finally: SEMPRE executa (com ou sem erro)
- raise: lança uma exceção manualmente
- Exceções personalizadas herdam de "Exception"
- Erros comuns: ZeroDivisionError, IndexError, KeyError,
  TypeError, ValueError, AttributeError
============================================================
"""
