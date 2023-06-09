class Produto:
    def __init__(self, nome, preco):
        self.__nome = nome
        self.__preco = preco

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_preco(self):
        return self.__preco

    def set_preco(self, preco):
        self.__preco = preco

    def calcular_valor_total(self, quantidade):
        return self.__preco * quantidade


class CarrinhoDeCompras:
    def __init__(self):
        self.__produtos = []

    def adicionar_produto(self, produto, quantidade):
        self.__produtos.append((produto, quantidade))

    def remover_produto(self, produto):
        for item in self.__produtos:
            if item[0] == produto:
                self.__produtos.remove(item)
                break

    def calcular_valor_total(self):
        total = 0
        for item in self.__produtos:
            produto = item[0]
            quantidade = item[1]
            total += produto.calcular_valor_total(quantidade)
        return total

    def get_produtos(self):
        return self.__produtos


produto1 = Produto("Camiseta", 59.9)
produto2 = Produto("Calça", 119.9)
produto3 = Produto("Tênis", 399.)

carrinho = CarrinhoDeCompras()

carrinho.adicionar_produto(produto1, 4)
carrinho.adicionar_produto(produto2, 2)
carrinho.adicionar_produto(produto3, 1)

produtos_no_carrinho = carrinho.get_produtos()
for item in produtos_no_carrinho:
    produto = item[0]
    quantidade = item[1]
    print("Produto:", produto.get_nome())
    print("Quantidade:", quantidade)
    print("Valor total:", produto.calcular_valor_total(quantidade))
    print()

valor_total = carrinho.calcular_valor_total()
print("Valor total do carrinho de compras:", valor_total)


carrinho.remover_produto(produto3)
carrinho.remover_produto(produto2)

valor_total = carrinho.calcular_valor_total()
print("Valor total do carrinho de compras com o produto 2 e 3 removido:", valor_total)
