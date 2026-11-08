import produtos
import clientes

#Funcao para cadastrar os produtos.
def cadastrar_produtos():

    cadastro = True
    while cadastro:

        while True:
            marca = input("Digite a marca do produto: ").strip()

            if not marca:
                print("Marca invalida, digite uma marca valida!")
                continue
            break

        while True:

            try:
                preco = float(input("Digite o valor do produto: "))
                estoque = int(input("Qual a quantidade do estoque: "))

                if preco <= 0 or estoque < 0:
                    print("Valor invalido, digite um valor maior que zero!")
                    continue
                break

            except ValueError:
                print("Valor invalido. Digite um numero valido!")
            
        item = produtos.Eletronicos(marca, preco, estoque)
        produtos.lista_produtos.append(item)

        cadastro = input("Deseja cadastrar outro produto? ").lower() == "sim"

#Funcao para colocar mais estoque.
def incluir_estoque():

    if not produtos.lista_produtos:
        print("Nenhum produto cadastrado. Cadastre um produto primeiro.")
        return

    inclusao = True
    while inclusao:
    
        decisao_estoque = input("Para qual produto? ").strip().lower()
        for item in produtos.lista_produtos:
            if item.marca.lower() == decisao_estoque:

                while True:
                    
                    try:
                            quantidade = int(input("Quantos produtos deseja adicionar? "))

                            if quantidade <= 0:
                                print("Digite uma quantidade maior que zero!")
                                continue

                            item.adicionar_estoque(quantidade)
                            print(f"Estoque atualizado de {item.marca}: {item.estoque}")
                            break

                    except ValueError:
                        print("Valor invalido. Digite um numero valido!")

                break
        else:
            print("Produto nao encontrado. Digite um produto cadastrado!")
            continue
            
        inclusao = input("Deseja adicionar mais produtos ao estoque? ").lower() == "sim"

#Funcao para mostrar os produtos.
def mostrar_produtos():

    if not produtos.lista_produtos:
        print("Nenhum produto cadastrado. Cadastre um produto primeiro.")
        return

    
    for item in produtos.lista_produtos:
        print("----------------------")
        print(f"Marca: {item.marca}")
        print(f"Preço: R$ {item.preco:.2f}")
        print(f"Estoque: {item.estoque}")
        print("----------------------")
            
#Funcao para cadastrar os cliente.
def cadastrar_clientes():

    cadastrar = True
    while cadastrar:

        while True:

            nome = input("Digite o nome do cliente: ").strip()
            endereco = input("Digite o endereco do cliente: ").strip()
            cpf = input("Digite o CPF do cliente: ").strip()

            cpf_existente = False
            for item in clientes.lista_cliente:
                if cpf == item.cpf:
                    cpf_existente = True
                    break

            if not nome or not cpf or not endereco:
                print("Dados invalidos. Por favor, preencha todos os campos.")
                continue

            if cpf_existente:
                print("CPF ja cadastrado. Digite um CPF diferente.")
                continue

            break

        usuario = clientes.Cliente(nome, cpf, endereco)
        clientes.lista_cliente.append(usuario)

        cadastrar = input("Deseja cadastrar outro cliente? ").lower() == "sim"

#Funcao para mostrar clientes.
def mostrar_cliente():

    if not clientes.lista_cliente:
        print("Nenhum cliente cadastrado. Cadastre um cliente primeiro.")
        return

    for usuario in clientes.lista_cliente:
        print("----------------------")
        print(f"Nome: {usuario.nome}")
        print(f"CPF: {usuario.cpf}")
        print(f"Endereco: {usuario.endereco}")
        print("----------------------")

#Funcao para realizar vendas.
def vendas():   

    if not produtos.lista_produtos:
        print("Nenhum produto cadastrado. Cadastre um produto primeiro.")
        return

    if not clientes.lista_cliente:
        print("Nenhum cliente cadastrado. Cadastre um cliente primeiro.")
        return

    #esse while serve para verificar se o cliente existe, e caso nao exista, ele pede para digitar um cliente cadastrado.
    c_encontrado = True
    while c_encontrado:

        cpf_cliente = input("Digite o CPF do cliente: ").strip()

        cliente_encontrado = None

        for usuario in clientes.lista_cliente:
            if cpf_cliente == usuario.cpf:
                cliente_encontrado = usuario
                break

        if cliente_encontrado is None:
            print(f"-----------------------")
            print("Cliente não encontrado. Digite um cliente cadastrado!")
            print(f"-----------------------")
        else:
            print(f"-----------------------")
            print(f"Cliente encontrado: {cliente_encontrado.nome}")
            print(f"-----------------------")
            c_encontrado = False
    
    #esse while serve para verificar se o produto existe, e caso nao exista, ele pede para digitar um produto cadastrado.
    p_encontrado = True
    while p_encontrado:

        nome_produto = input("Digite o produto que deseja vender: ").strip().lower()

        produto_encontrado = None

        for item in produtos.lista_produtos:
            if nome_produto == item.marca.lower():
                produto_encontrado = item
                break

        if produto_encontrado is None:
            print(f"-----------------------")
            print("Produto não encontrado. Digite um produto cadastrado!")
            print(f"-----------------------")
        else:
            if produto_encontrado.estoque == 0:
                print("Produto sem estoque!")
                continue

            print(f"-----------------------")
            print(f"Produto encontrado: {produto_encontrado.marca}")
            print(f"-----------------------")
            p_encontrado = False

    v_quantidade = True
    while v_quantidade:

        try:
            quantidade = int(input("Digite a quantidade que deseja vender: "))
        
            if quantidade <= 0:
                print("Quantidade inválida. Digite um valor maior que zero.")
                continue

        except ValueError:
            print("Valor invalido. Digite um numero valido!")
            continue

        if quantidade <= produto_encontrado.estoque:
            produto_encontrado.remover_estoque(quantidade)
            total = produto_encontrado.preco * quantidade

            print("Venda realizada com sucesso!")
            cliente_encontrado.registrar_compra(
                produto_encontrado.marca,
                quantidade,
                total
            )
            print(f"Produto: {produto_encontrado.marca}")
            print(f"Quantidade: {quantidade}")
            print(f"Valor total: R$ {total:.2f}")
            print(f"Estoque restante: {produto_encontrado.estoque}")
            v_quantidade = False
                    
        else:
            print("Estoque insuficiente para realizar a venda. Digite uma quantidade menor ou igual ao estoque disponível.")

#Funcao para mostrar as compras realizadas por cada cliente.
def mostrar_compras():

    if not clientes.lista_cliente:
        print("Nenhum cliente cadastrado. Cadastre um cliente primeiro.")
        return

    for usuario in clientes.lista_cliente:
        print(f"Compras do cliente {usuario.nome}:")
        if usuario.compras:
            for compra in usuario.compras:
                print(f"- Produto: {compra['produto']}, Quantidade: {compra['quantidade']}, Valor total: R$ {compra['valor_total']:.2f}")
        else:
            print("Nenhuma compra realizada.")
        print("----------------------")

#Parte principal do programa.
menu = True
while menu:
    print("\nMENU - LOJA DE ELETRONICOS")
    print("--------------------------")
    print("1 PRODUTOS")
    print("2 CLIENTES")
    print("3 REALIZAR UMA VENDA")
    print("4 MOSTRAR COMPRAS")
    print("5 SAIR")
    print("--------------------------")
    decisao = input("QUAL OPCAO DESEJA? ")

    if decisao == "1":
        
        print("\n1 CADASTRAR NOVO PRODUTO")
        print("2 INCLUIR ESTOQUE")
        print("3 MOSTRAR PRODUTOS")
        print("4 VOLTAR AO MENU")
        decisao1 = input("O QUE DESEJA FAZER? ")

        if decisao1 == "1":
            cadastrar_produtos()
        elif decisao1 == "2":
            incluir_estoque()
        elif decisao1 == "3":
            mostrar_produtos()
        elif decisao1 == "4":
            print("Voltando ao menu...")
        else:
            print("-----------------------")
            print("Opção inválida! Digite uma opção de 1 a 4.")
            print("-----------------------")

    elif decisao == "2":

        print("\n1- CADASTRAR CLIENTES")
        print("2- MOSTRAR CLIENTES")
        print("3- VOLTAR AO MENU")
        decisao2 = input("O QUE DESEJA FAZER? ")

        if decisao2 == "1":
            cadastrar_clientes()
        elif decisao2 == "2":
            mostrar_cliente()
        elif decisao2 == "3":
            print("Voltando ao menu...")
        else:
            print("-----------------------")
            print("Opção inválida! Digite uma opção de 1 a 3.")
            print("-----------------------")

    elif decisao == "3":

        print("\n1- REALIZAR UMA VENDA")
        print("2- VOLTAR AO MENU")
        decisao4 = input("O QUE DESEJA FAZER? ")

        if decisao4 == "1":
            vendas()
        elif decisao4 == "2":
            print("Voltando ao menu...")
        else:
            print("-----------------------")
            print("Opção inválida! Digite uma opção de 1 a 2.")
            print("-----------------------")

    elif decisao == "4":
    
        print("\n1- MOSTRAR COMPRAS")
        print("2- VOLTAR AO MENU")
        decisao3 = input("O QUE DESEJA FAZER? ")
    
        if decisao3 == "1":
            mostrar_compras()
        elif decisao3 == "2":
            print("Voltando ao menu...")
        else:
            print("-----------------------")
            print("Opção inválida! Digite uma opção de 1 a 2.")
            print("-----------------------")

    elif decisao == "5":
        print("Saindo do programa...")
        menu = False

    else:
        print("-----------------------")
        print("Opção inválida! Digite uma opção de 1 a 5.")
        print("-----------------------")