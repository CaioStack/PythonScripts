"""
============================================================
 EXERCÍCIO 13 - ENCAPSULAMENTO, PROPRIEDADES E CLASSES ABSTRATAS
 (referente à aula13.py)
============================================================

ENUNCIADO:
1) Crie uma classe "Funcionario" ENCAPSULADA com:
   - Atributo "privado" __salario (definido no __init__)
   - Uma @property "salario" para leitura
   - Um @salario.setter que só permite valores >= 0
   - Um método aumentar_salario(percentual) que aumenta o
     salário em X% (ex.: 10 significa 10%)
2) Crie a classe abstrata "Forma" (usando ABC) com o método
   abstrato calcular_perimetro().
3) Crie as subclasses "Quadrado" e "Triangulo" (equilátero),
   cada uma implementando calcular_perimetro() do seu jeito.
4) No bloco principal, teste o encapsulamento (inclusive uma
   tentativa de salário inválido) e teste o polimorfismo das
   formas geométricas.
"""

from abc import ABC, abstractmethod


class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.__salario = max(salario, 0)

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, novo_salario):
        if novo_salario >= 0:
            self.__salario = novo_salario
        else:
            print("Salário inválido! Deve ser maior ou igual a zero.")

    def aumentar_salario(self, percentual):
        self.__salario += self.__salario * (percentual / 100)

    def __str__(self):
        return f"{self.nome} - Salário: R$ {self.__salario:.2f}"


class Forma(ABC):
    @abstractmethod
    def calcular_perimetro(self):
        pass


class Quadrado(Forma):
    def __init__(self, lado):
        self.lado = lado

    def calcular_perimetro(self):
        return self.lado * 4


class Triangulo(Forma):
    def __init__(self, lado):
        self.lado = lado  # triângulo equilátero: todos os lados iguais

    def calcular_perimetro(self):
        return self.lado * 3


if __name__ == "__main__":
    # TODO 1: testando o encapsulamento
    funcionario = Funcionario("Camila Torres", 3500.0)
    print(funcionario)

    funcionario.aumentar_salario(10)
    print(f"Após aumento de 10%: {funcionario}")

    funcionario.salario = -500  # o setter vai bloquear
    print(f"Após tentativa inválida: {funcionario}")

    # TODO 2, 3 e 4: testando o polimorfismo das formas
    formas = [Quadrado(5), Triangulo(6)]
    print("\n--- Perímetros ---")
    for forma in formas:
        print(f"{type(forma).__name__} -> Perímetro: {forma.calcular_perimetro()}")
