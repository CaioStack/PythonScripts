"""
============================================================
 EXERCÍCIO 11 - CLASSES E OBJETOS
 (referente à aula11.py)
============================================================

ENUNCIADO:
Crie uma classe "Produto" com:
  - Atributos definidos no __init__: nome (str), preco (float),
    quantidade_estoque (int)
  - Métodos:
      exibir_informacoes(self) -> imprime os dados do produto
      calcular_valor_total(self) -> retorna preco * quantidade_estoque
      vender_unidade(self) -> diminui 1 do estoque (se houver estoque)
  - Um método __str__ que retorna uma representação legível do produto

No bloco "if __name__ == '__main__':":
  1) Crie 2 objetos Produto diferentes.
  2) Exiba as informações de cada um.
  3) Venda algumas unidades de um dos produtos.
  4) Exiba o valor total em estoque de cada produto.
"""


class Produto:
    def __init__(self, nome, preco, quantidade_estoque):
        self.nome = nome
        self.preco = preco
        self.quantidade_estoque = quantidade_estoque

    def exibir_informacoes(self):
        print(f"\nProduto: {self.nome}")
        print(f"Preço: R$ {self.preco}")
        print(f"Estoque: {self.quantidade_estoque} unidades")

    def calcular_valor_total(self):
        return self.preco * self.quantidade_estoque

    def vender_unidade(self):
        if self.quantidade_estoque > 0:
            self.quantidade_estoque -= 1
        else:
            print(f"Produto {self.nome} sem estoque!")

    def __str__(self):
        return f"Produto(nome={self.nome}, preco={self.preco}, estoque={self.quantidade_estoque})"


if __name__ == "__main__":
    # TODO 1: criar os objetos
    produto1 = Produto("Notebook", 3200.00, 10)
    produto2 = Produto("Mouse sem fio", 79.90, 50)

    # TODO 2: exibir informações
    produto1.exibir_informacoes()
    produto2.exibir_informacoes()

    # TODO 3: vender algumas unidades
    produto2.vender_unidade()
    produto2.vender_unidade()
    produto2.vender_unidade()

    # TODO 4: exibir valor total em estoque
    print(f"\nValor total em estoque - {produto1.nome}: R$ {produto1.calcular_valor_total()}")
    print(f"Valor total em estoque - {produto2.nome}: R$ {produto2.calcular_valor_total()}")
    print(f"Estoque restante de {produto2.nome}: {produto2.quantidade_estoque}")
