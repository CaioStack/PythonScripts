"""
============================================================
 AULA 13 - ENCAPSULAMENTO, PROPRIEDADES E CLASSES ABSTRATAS
============================================================

ENCAPSULAMENTO em Python funciona DIFERENTE do Java: não existe
"private" de verdade, a linguagem usa CONVENÇÕES DE NOME:

  atributo        -> público (acesso livre, uso normal)
  _atributo        -> "protegido" por convenção (uso interno,
                       mas nada impede o acesso de fora)
  __atributo        -> "privado" por convenção (o Python faz um
                       "name mangling", dificultando o acesso
                       direto de fora da classe)

Para ter GETTERS e SETTERS "de verdade" com validação, usamos o
decorador @property, que é a forma "pythônica" de fazer isso.

CLASSE ABSTRATA: assim como no Java, uma classe que não pode ser
instanciada diretamente, servindo de modelo para subclasses. Em
Python usamos o módulo "abc" (Abstract Base Classes).
"""

from abc import ABC, abstractmethod


# ---------------- ENCAPSULAMENTO COM @property ----------------
class ContaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular              # atributo público
        self.__saldo = max(saldo_inicial, 0)  # atributo "privado" (name mangling)

    # @property transforma um método em um "getter", acessado SEM
    # parênteses (como se fosse um atributo comum): conta.saldo
    @property
    def saldo(self):
        return self.__saldo

    # @saldo.setter permite ATRIBUIR valor através de conta.saldo = valor,
    # mas passando pela validação definida aqui
    @saldo.setter
    def saldo(self, novo_saldo):
        if novo_saldo >= 0:
            self.__saldo = novo_saldo
        else:
            print("Não é possível definir um saldo negativo diretamente.")

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor

    def sacar(self, valor):
        if valor <= 0:
            print("Valor de saque inválido.")
        elif valor > self.__saldo:
            print(f"Saldo insuficiente para {self.titular} sacar R$ {valor}")
        else:
            self.__saldo -= valor


# ---------------- CLASSE ABSTRATA (módulo abc) ----------------
class FormaGeometrica(ABC):  # herdar de ABC torna a classe abstrata

    @abstractmethod
    def calcular_area(self):
        """Método abstrato: cada subclasse é OBRIGADA a implementar."""
        pass  # sem corpo real, só a assinatura

    # Classes abstratas TAMBÉM podem ter métodos concretos (com corpo)
    def identificar(self):
        print("Eu sou uma forma geométrica.")


class Circulo(FormaGeometrica):
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return 3.14159 * self.raio ** 2


class Retangulo(FormaGeometrica):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        return self.largura * self.altura


if __name__ == "__main__":
    # ---------------- TESTANDO O ENCAPSULAMENTO ----------------
    conta = ContaBancaria("Fernanda", 1000.0)

    # Não conseguimos acessar conta.__saldo diretamente de fora (name mangling)!
    # print(conta.__saldo)  # <- geraria AttributeError

    print(f"{conta.titular} tem saldo de R$ {conta.saldo}")  # usa o @property (sem parênteses!)

    conta.depositar(500.0)
    print(f"Após depósito: R$ {conta.saldo}")

    conta.sacar(200.0)
    print(f"Após saque: R$ {conta.saldo}")

    conta.saldo = 2000  # usa o @saldo.setter (com validação)
    print(f"Saldo definido diretamente: R$ {conta.saldo}")

    conta.saldo = -500  # o setter vai BLOQUEAR essa tentativa
    print(f"Saldo após tentativa inválida: R$ {conta.saldo}")

    # ---------------- TESTANDO A CLASSE ABSTRATA ----------------
    formas = [Circulo(5), Retangulo(4, 6)]
    for forma in formas:
        print(f"{type(forma).__name__} -> Área: {forma.calcular_area():.2f}")

    # forma_generica = FormaGeometrica()  # <- ERRO! Não é possível
    # instanciar uma classe abstrata diretamente (TypeError)

"""
------------------------------------------------------------
RESUMO DA AULA
------------------------------------------------------------
- _atributo: "protegido" por convenção
- __atributo: "privado" por convenção (name mangling)
- @property cria um GETTER acessado como atributo (sem parênteses)
- @nome.setter cria um SETTER com validação, usado com "objeto.nome = valor"
- ABC + @abstractmethod criam classes e métodos abstratos, como no Java
============================================================
"""
