"""
============================================================
 EXERCÍCIO 12 - HERANÇA E POLIMORFISMO
 (referente à aula12.py)
============================================================

ENUNCIADO:
Crie uma hierarquia de veículos:
  - Classe "Veiculo" (superclasse): atributos modelo (str) e
    velocidade_atual (float, inicia em 0). Métodos: acelerar(incremento)
    que soma na velocidade atual, frear() que zera a velocidade,
    e exibir_status() que imprime modelo + velocidade atual.
  - Classe "Carro" (herda de Veiculo): atributo extra numero_portas (int).
    Sobrescreva exibir_status() para também mostrar o número de portas.
  - Classe "Moto" (herda de Veiculo): atributo extra cilindradas (int).
    Sobrescreva exibir_status() para também mostrar as cilindradas.

No bloco principal, crie um Carro e uma Moto, acelere ambos, e
chame exibir_status() de cada um. Depois, crie uma lista com os
dois veículos e percorra chamando exibir_status() de cada um
(demonstrando polimorfismo).
"""


class Veiculo:
    def __init__(self, modelo):
        self.modelo = modelo
        self.velocidade_atual = 0

    def acelerar(self, incremento):
        self.velocidade_atual += incremento

    def frear(self):
        self.velocidade_atual = 0

    def exibir_status(self):
        print(f"Modelo: {self.modelo} | Velocidade atual: {self.velocidade_atual} km/h")


class Carro(Veiculo):
    def __init__(self, modelo, numero_portas):
        super().__init__(modelo)
        self.numero_portas = numero_portas

    def exibir_status(self):
        super().exibir_status()  # reaproveita a lógica da superclasse
        print(f"Número de portas: {self.numero_portas}")


class Moto(Veiculo):
    def __init__(self, modelo, cilindradas):
        super().__init__(modelo)
        self.cilindradas = cilindradas

    def exibir_status(self):
        super().exibir_status()
        print(f"Cilindradas: {self.cilindradas}cc")


if __name__ == "__main__":
    meu_carro = Carro("Civic", 4)
    minha_moto = Moto("CB 500", 500)

    meu_carro.acelerar(60)
    minha_moto.acelerar(80)

    meu_carro.exibir_status()
    minha_moto.exibir_status()

    meu_carro.frear()
    print("\nApós frear:")
    meu_carro.exibir_status()

    # Demonstrando polimorfismo com uma lista de veículos
    print("\n--- Percorrendo todos os veículos ---")
    veiculos = [meu_carro, minha_moto]
    for veiculo in veiculos:
        veiculo.exibir_status()
        print("------")
