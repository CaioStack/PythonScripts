"""
============================================================
 AULA 09 - FUNÇÕES
============================================================

Uma FUNÇÃO é um bloco de código reutilizável, que executa uma
tarefa específica. Funções ajudam a organizar o código, evitar
repetição e facilitar testes e manutenção.

ESTRUTURA GERAL:
  def nome_da_funcao(parametros):
      # corpo da função
      return valor  # opcional; se não tiver, a função retorna None

DIFERENÇA IMPORTANTE EM RELAÇÃO AO JAVA:
- Não é preciso declarar o TIPO de retorno nem dos parâmetros
- Funções em Python podem ficar SOLTAS no arquivo (não precisam
  estar dentro de uma classe)
"""


# ---------------- FUNÇÃO SEM PARÂMETRO E SEM RETORNO ----------------
def saudacao():
    print("Olá! Bem-vindo(a) à aula de funções.")


# ---------------- FUNÇÃO COM PARÂMETRO ----------------
def saudacao_com_nome(nome):
    print(f"Olá, {nome}!")


# ---------------- FUNÇÃO COM RETORNO ----------------
def somar(a, b):
    return a + b  # "return" devolve o valor para quem chamou a função


# Função com múltiplos parâmetros
def calcular_media(nota1, nota2, nota3):
    return (nota1 + nota2 + nota3) / 3


# Função que retorna um bool
def eh_par(numero):
    return numero % 2 == 0


# ---------------- PARÂMETROS COM VALOR PADRÃO (default) ----------------
# Se o argumento não for informado na chamada, usa o valor padrão
def calcular_area_retangulo(largura, altura=1):
    return largura * altura


# ---------------- ARGUMENTOS NOMEADOS (keyword arguments) ----------------
def apresentar_pessoa(nome, idade, cidade="Não informado"):
    print(f"{nome}, {idade} anos, de {cidade}")


# ---------------- *args: quantidade VARIÁVEL de argumentos ----------------
# Equivalente ao "varargs" (tipo... nome) do Java
def somar_varios(*numeros):
    soma = 0
    for numero in numeros:
        soma += numero
    return soma


# ---------------- **kwargs: quantidade VARIÁVEL de argumentos nomeados ----------------
def exibir_dados(**dados):
    for chave, valor in dados.items():
        print(f"{chave}: {valor}")


# ---------------- FUNÇÃO RECEBENDO UMA LISTA ----------------
def encontrar_maior(numeros):
    maior = numeros[0]
    for numero in numeros:
        if numero > maior:
            maior = numero
    return maior


# ---------------- FUNÇÃO RETORNANDO MÚLTIPLOS VALORES (recurso do Python) ----------------
# Em Java, para "retornar" mais de um valor, seria preciso criar uma
# classe/objeto. Em Python, basta retornar uma tupla!
def calcular_estatisticas(numeros):
    maior = max(numeros)
    menor = min(numeros)
    media = sum(numeros) / len(numeros)
    return maior, menor, media  # retorna uma tupla (maior, menor, media)


# ---------------- CHAMANDO AS FUNÇÕES ----------------
if __name__ == "__main__":
    # O bloco "if __name__ == '__main__':" garante que este código só
    # roda quando o ARQUIVO é executado diretamente (não quando ele é
    # importado por outro arquivo). É uma boa prática comum em Python,
    # parecida em espírito com o "main" do Java.

    saudacao()
    saudacao_com_nome("Carlos")

    resultado_soma = somar(5, 7)
    print(f"Resultado da soma: {resultado_soma}")

    media = calcular_media(8.0, 6.5, 9.0)
    print(f"Média calculada: {media}")

    print(f"10 é par? {eh_par(10)}")

    print(f"Área (só largura, altura padrão=1): {calcular_area_retangulo(5)}")
    print(f"Área (largura e altura): {calcular_area_retangulo(5, 3)}")

    apresentar_pessoa("Maria", 28)  # usa o valor padrão de cidade
    apresentar_pessoa(nome="João", idade=35, cidade="Fortaleza")  # argumentos nomeados

    print(f"Soma de vários números: {somar_varios(1, 2, 3, 4, 5)}")

    print("\n--- Dados de uma pessoa (**kwargs) ---")
    exibir_dados(nome="Ana", idade=22, profissao="Desenvolvedora")

    numeros = [4, 8, 15, 16, 23, 42]
    print(f"\nMaior número da lista: {encontrar_maior(numeros)}")

    maior, menor, media = calcular_estatisticas(numeros)
    print(f"Estatísticas -> maior: {maior}, menor: {menor}, média: {media:.2f}")

"""
------------------------------------------------------------
RESUMO DA AULA
------------------------------------------------------------
- def nome(parametros): define uma função
- "return" devolve um valor (ou None, se omitido)
- parâmetros podem ter VALOR PADRÃO: def f(x, y=10)
- *args recebe quantidade variável de argumentos posicionais
- **kwargs recebe quantidade variável de argumentos nomeados
- funções podem retornar MÚLTIPLOS valores usando tuplas
- if __name__ == "__main__": indica o ponto de entrada do script
============================================================
"""
