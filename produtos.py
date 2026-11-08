class Eletronicos:
    def __init__(self, marca, preco, estoque):

        self.marca = marca
        self.preco = preco
        self.estoque = estoque

    def adicionar_estoque(self, quantidade):
        self.estoque += quantidade

    def remover_estoque(self, quantidade):
        self.estoque -= quantidade
       
lista_produtos = []