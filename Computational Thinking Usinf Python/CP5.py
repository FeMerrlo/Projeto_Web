nome_cliente = input("Digite o seu nome: ")
qtd_produtos = int(input("Digite a quantidade de produtos que deseja comprar: "))


produtos = []
for i in range(qtd_produtos):
    print(f"Digite as informações do produto {i + 1}:")
    nome = input("Nome do produto: ")
    qtd = int(input("Quantidade: "))
    preco_unitario = float(input("Preço unitário: "))
    produtos.append((nome, qtd, preco_unitario))


try:
    arquivo = open("pedidos.txt", "a")
    arquivo.write(nome_cliente + "\n")
    for nome, qtd, preco_unitario in produtos:
        arquivo.write(f"{nome},{qtd},{preco_unitario}\n")
        
finally:
    arquivo.close()
    

opcao = input("Deseja cadastrar um novo pedido? (s/n): ")
if opcao == "s":


    nome_cliente = input("Digite o seu nome: ")
    qtd_produtos = int(input("Digite a quantidade de produtos que deseja comprar: "))

   
    produtos = []
    for i in range(qtd_produtos):
        print(f"Digite as informações do produto {i + 1}:")
        nome = input("Nome do produto: ")
        qtd = int(input("Quantidade: "))
        preco_unitario = float(input("Preço unitário: "))
        produtos.append((nome, qtd, preco_unitario))


    try:
        arquivo = open("pedidos.txt", "a")
        arquivo.write(nome_cliente + "\n")
        for nome, qtd, preco_unitario in produtos:
            arquivo.write(f"{nome},{qtd},{preco_unitario}\n")
    finally:
        arquivo.close()

total_clientes = {}
try:
    arquivo = open("pedidos.txt", "r")
    nome_cliente = ""
    for linha in arquivo:
        if linha != "":
            if nome_cliente == "":
                nome_cliente = linha
                total_clientes[nome_cliente] = 0
            else:
                nome_produto, quantidade, preco_unitario = linha.split(",")
                quantidade = int(quantidade)
                preco_unitario = float(preco_unitario)
                valor_total_produto = quantidade * preco_unitario
                total_clientes[nome_cliente] += valor_total_produto
        else:
            nome_cliente = ""
finally:
    arquivo.close()


try:
    arquivo = open("valor_pedidos.txt", "w")
    for nome_cliente, valor_total in total_clientes.items():
        arquivo.write(f"{nome_cliente}: R${valor_total:.2f}\n")
finally:
    arquivo.close()

total_clientes = {}
arquivo = open("pedidos.txt", "r")
nome_cliente = ""
for linha in arquivo:
    linha = linha.replace('\n', '')
    if linha != "":
        if nome_cliente == "":
            nome_cliente = linha
            total_clientes[nome_cliente] = 0
        else:
            nome_produto, quantidade, preco_unitario = linha.split(",")
            quantidade = int(quantidade)
            preco_unitario = float(preco_unitario)
            valor_total_produto = quantidade * preco_unitario
            total_clientes[nome_cliente] += valor_total_produto
    else:
        nome_cliente = ""
arquivo.close()

arquivo = open("total_pedidos.txt", "w")
for nome_cliente, valor_total in total_clientes.items():
    arquivo.write(f"{nome_cliente}: R${valor_total:.2f}\n")
arquivo.close()


print("Programa finalizado.")
