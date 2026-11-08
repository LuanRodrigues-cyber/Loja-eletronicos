class Cliente:
    def __init__(self, nome, cpf, endereco):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
        self.compras = []  # Lista para armazenar as compras do cliente

    def registrar_compra(self, produto, quantidade, valor_total):
        self.compras.append({
            "produto": produto,
            "quantidade": quantidade,
            "valor_total": valor_total
        })

lista_cliente = []