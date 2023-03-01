clientes = {}
contas_bancarias = set()

while True:
    nome = input("Digite o nome do cliente (ou 'sair' para encerrar): ")
    if nome == "sair":
        break
    email = input("Digite o email do cliente: ")
    idade = int(input("Digite a idade do cliente: "))
    clientes[nome] = (email, idade)
    
    tem_conta = input("O cliente possui conta bancária? (sim/não) ")
    if tem_conta == "sim":
        agencia = input("Digite a agência bancária: ")
        numero = input("Digite o número da conta: ")
        saldo = float(input("Digite o saldo da conta: "))
        contas_bancarias.add((agencia, numero, saldo, nome))

print("Clientes cadastrados:")
for nome, dados in clientes.items():
    email, idade = dados
    print(f"Nome: {nome}, Email: {email}, Idade: {idade}")
    for agencia, numero, saldo, titular in contas_bancarias:
        if titular == nome:
            print(f"Conta bancária: Agência {agencia}, Número {numero}, Saldo R$ {saldo}")


