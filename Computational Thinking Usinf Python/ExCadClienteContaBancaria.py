clientes=[]
emails = {}

print('Cadastro de Clientes')

while(True):
    print('1 - Incluir')
    print('2 - Atualizar')
    print('3 - Excluir')
    print('4 - Exibir')
    print('5 - Incluir')
    opcao = int(input('Digite a opção escolhida: '))
    
    if (opcao == 1):
        nome = input('Digite o seu nome: ')
        email = input('Digite o seu email: ')
        
        if (email in emails):
            print('Esse email já faz parte de outro cadastro. Escoha outro')
            email = input('Digite o seu email: ')
        
        possuiConta = input('Possui conta bancária ? S/N')