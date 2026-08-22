"""
============================================================
 EXERCÍCIO 14 - TRATAMENTO DE EXCEÇÕES
 (referente à aula14.py)
============================================================

ENUNCIADO:
1) Crie uma função dividir(a, b) que trata a divisão por zero
   com try/except e retorna 0 nesse caso (sem quebrar o programa).
2) Peça ao usuário para digitar um número via input(). Trate o
   caso do usuário digitar um texto inválido (ValueError).
3) Crie uma exceção personalizada "IdadeInvalidaError" e uma
   função cadastrar_idade(idade) que a lança se idade < 0 ou
   idade > 120.
4) No programa, teste todos os cenários (incluindo os de erro)
   para garantir que o programa NUNCA quebre inesperadamente.
"""


# TODO 1: divisão segura
def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Aviso: divisão por zero detectada, retornando 0.")
        return 0


# TODO 3: exceção personalizada
class IdadeInvalidaError(Exception):
    """Exceção lançada quando uma idade está fora do intervalo permitido."""
    pass


def cadastrar_idade(idade):
    if idade < 0 or idade > 120:
        raise IdadeInvalidaError(f"Idade fora do intervalo permitido (0 a 120): {idade}")
    print(f"Idade {idade} cadastrada com sucesso!")


if __name__ == "__main__":
    # TODO 1: testando o método dividir
    print(f"10 / 2 = {dividir(10, 2)}")
    print(f"10 / 0 = {dividir(10, 0)}")  # não deve quebrar o programa

    # TODO 2: leitura segura de número
    entrada = input("\nDigite um número inteiro: ")
    try:
        numero = int(entrada)
        print(f"Você digitou: {numero}")
    except ValueError:
        print("Erro: isso não é um número inteiro válido!")

    # TODO 3 e 4: testando a exceção personalizada
    idades_para_testar = [25, -5, 200]
    for idade in idades_para_testar:
        try:
            cadastrar_idade(idade)
        except IdadeInvalidaError as erro:
            print(f"Erro ao cadastrar idade {idade}: {erro}")

    print("\nPrograma finalizado sem quebrar!")
