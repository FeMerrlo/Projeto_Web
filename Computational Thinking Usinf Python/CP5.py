nome_cliente = input("Digite o seu nome: ")
qtd_produtos = int(input("Digite a quantidade de produtos que deseja comprar: "))


produtos = []
for i in range(qtd_produtos):
    print(f"Digite as informações do produto {i + 1}:")
    nome = input("Nome do produto: ")
    qtd = int(input("Quantidade: "))
    preco_unitario = float(input("Preço unitário: "))
    produtos.append((nome, qtd, preco_unitario))


with open("pedidos.txt", "w") as arquivo:
    arquivo.write(nome_cliente + "\n")
    for nome, qtd, preco_unitario in produtos:
        arquivo.write(f"{nome},{qtd},{preco_unitario}\n")

opcao = input("Deseja cadastrar um novo pedido? (s/n): ")
if opcao.lower() == "s":

    nome_cliente = input("Digite o seu nome: ")
    qtd_produtos = int(input("Digite a quantidade de produtos que deseja comprar: "))

   
    produtos = []
    for i in range(qtd_produtos):
        print(f"Digite as informações do produto {i + 1}:")
        nome = input("Nome do produto: ")
        qtd = int(input("Quantidade: "))
        preco_unitario = float(input("Preço unitário: "))
        produtos.append((nome, qtd, preco_unitario))


    arquivo.write(nome_cliente + "\n")
    for nome, qtd, preco_unitario in produtos:
        arquivo.write(f"{nome},{qtd},{preco_unitario}\n")

total_clientes = {}
with open("pedidos.txt", "r") as arquivo:
    nome_cliente = ""
    for linha in arquivo:
        linha = linha.strip()
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


with open("valor_pedidos.txt", "w") as arquivo:
    for nome_cliente, valor_total in total_clientes.items():
        arquivo.write(f"{nome_cliente}: R${valor_total:.2f}\n")


print("Programa finalizado.")
