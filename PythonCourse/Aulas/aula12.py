"""
============================================================
 AULA 12 - HERANÇA E POLIMORFISMO
============================================================

HERANÇA permite que uma classe (SUBCLASSE) reaproveite atributos
e métodos de outra classe (SUPERCLASSE), evitando duplicação de
código. Em Python, a sintaxe é: class Filha(Mae):

POLIMORFISMO: capacidade de tratar objetos de subclasses
diferentes de forma UNIFORME, mas cada um se comportando à sua
própria maneira.
"""


# ---------------- SUPERCLASSE (classe pai) ----------------
class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def dormir(self):
        print(f"{self.nome} está dormindo... zzz")

    # Método que pode ser SOBRESCRITO pelas subclasses
    def emitir_som(self):
        print(f"{self.nome} emite um som genérico de animal.")

    def exibir_informacoes(self):
        print(f"Nome: {self.nome} | Idade: {self.idade} ano(s)")


# ---------------- SUBCLASSES (classes filhas) ----------------
# class Cachorro(Animal): significa que Cachorro HERDA tudo de Animal
class Cachorro(Animal):
    def __init__(self, nome, idade):
        # super().__init__(...) chama o construtor da SUPERCLASSE
        super().__init__(nome, idade)

    # Método específico do Cachorro (Animal não tem)
    def latir(self):
        print(f"{self.nome} está latindo: Au au!")

    # SOBRESCREVENDO (override) o método da superclasse
    # Python não exige uma anotação como @Override do Java, mas
    # podemos usar @override (typing) opcionalmente para documentar
    def emitir_som(self):
        print(f"{self.nome} (cachorro) faz: Au au!")


class Gato(Animal):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)

    def miar(self):
        print(f"{self.nome} está miando: Miau!")

    def emitir_som(self):
        print(f"{self.nome} (gato) faz: Miau!")


if __name__ == "__main__":
    rex = Cachorro("Rex", 3)
    mimi = Gato("Mimi", 2)

    # Métodos herdados da superclasse Animal
    rex.dormir()
    mimi.dormir()

    # Métodos ESPECÍFICOS de cada subclasse
    rex.latir()
    mimi.miar()

    # Método SOBRESCRITO - cada subclasse tem seu próprio "emitir_som"
    rex.emitir_som()
    mimi.emitir_som()

    # Método herdado que usa dados da superclasse
    rex.exibir_informacoes()
    mimi.exibir_informacoes()

    # ---------------- POLIMORFISMO EM AÇÃO ----------------
    # Uma lista de "Animal" pode conter objetos de QUALQUER subclasse,
    # e cada um se comporta à sua própria maneira ao chamar o MESMO método
    animais = [Cachorro("Bidu", 1), Gato("Frajola", 4), Cachorro("Thor", 2)]

    print("\n--- Percorrendo todos os animais (polimorfismo) ---")
    for animal in animais:
        animal.emitir_som()  # chama a versão CORRETA de cada subclasse

    # isinstance() verifica o tipo de um objeto em tempo de execução
    print(f"\nrex é um Cachorro? {isinstance(rex, Cachorro)}")
    print(f"rex é um Animal? {isinstance(rex, Animal)}")  # True! (herança)
    print(f"rex é um Gato? {isinstance(rex, Gato)}")

"""
------------------------------------------------------------
RESUMO DA AULA
------------------------------------------------------------
- class Filha(Mae): cria uma relação de herança
- super().__init__(...) chama o construtor da classe pai
- Sobrescrever um método: basta redefini-lo na subclasse com o
  MESMO nome (Python não exige anotação especial, mas @override
  do módulo typing pode documentar a intenção)
- Polimorfismo: tratar objetos diferentes de forma uniforme
- isinstance(objeto, Classe) verifica o tipo em tempo de execução
- Python permite HERANÇA MÚLTIPLA (uma classe pode herdar de
  VÁRIAS outras), diferente do Java que só permite herança simples
============================================================
"""
