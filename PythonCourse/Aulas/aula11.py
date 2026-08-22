"""
============================================================
 AULA 11 - INTRODUÇÃO À POO: CLASSES E OBJETOS
============================================================

A partir de agora entramos em Programação Orientada a Objetos
(POO) em Python. Os conceitos são os MESMOS do Java (classe,
objeto, atributos, métodos), mas a sintaxe é diferente.

DIFERENÇAS IMPORTANTES EM RELAÇÃO AO JAVA:
- O construtor se chama __init__ (não tem o nome da classe)
- Todo método de instância recebe "self" como PRIMEIRO parâmetro,
  representando o próprio objeto (equivalente ao "this" do Java,
  mas precisa ser declarado explicitamente!)
- Não existe "public"/"private" de verdade; usamos convenções
  (veremos isso em detalhe na próxima aula)
"""


class Pessoa:
    # ---------------- CONSTRUTOR ----------------
    # __init__ é chamado automaticamente ao criar um objeto com Pessoa(...)
    def __init__(self, nome, idade):
        # "self.nome" cria um ATRIBUTO no objeto sendo criado
        self.nome = nome
        self.idade = idade

    # ---------------- MÉTODOS (comportamentos) ----------------
    # Todo método de instância recebe "self" como primeiro parâmetro
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

    def fazer_aniversario(self):
        self.idade += 1  # incrementa a idade DESTE objeto específico

    def eh_maior_de_idade(self):
        return self.idade >= 18

    # ---------------- MÉTODO ESPECIAL __str__ ----------------
    # Define como o objeto é exibido quando usamos print(objeto)
    # (equivalente a sobrescrever o toString() do Java)
    def __str__(self):
        return f"Pessoa(nome={self.nome}, idade={self.idade})"


if __name__ == "__main__":
    # Criando (instanciando) objetos da classe Pessoa
    # Repare que NÃO usamos a palavra "new" como no Java!
    pessoa1 = Pessoa("Mariana", 25)
    pessoa2 = Pessoa("Pedro", 30)

    # Cada objeto tem seus PRÓPRIOS valores de atributos
    print(f"{pessoa1.nome} tem {pessoa1.idade} anos.")
    print(f"{pessoa2.nome} tem {pessoa2.idade} anos.")

    # Chamando métodos (comportamentos) dos objetos
    pessoa1.apresentar()
    pessoa2.apresentar()

    pessoa1.fazer_aniversario()
    print(f"{pessoa1.nome} agora tem {pessoa1.idade} anos.")

    # Verificando se a pessoa é maior de idade (método que retorna bool)
    print(f"{pessoa2.nome} é maior de idade? {pessoa2.eh_maior_de_idade()}")

    # Usando o método especial __str__
    print(f"\nRepresentação do objeto: {pessoa1}")

"""
------------------------------------------------------------
RESUMO DA AULA
------------------------------------------------------------
- class NomeDaClasse: define uma classe
- __init__(self, ...) é o construtor
- self representa o PRÓPRIO objeto (como o "this" do Java, mas
  precisa ser declarado como parâmetro explicitamente)
- Objetos são criados chamando a classe como uma função: Pessoa(...)
  (sem a palavra "new")
- __str__(self) define como o objeto aparece no print()
============================================================
"""
