
numeros = []
posi = -1
QdV = int(input('Quantos valores você deseja adicionar a lista: '))
while(QdV <= 0 or QdV > 20 ):
    print('Eita, a quantidade maxima é 20')
    QdV = int(input('Digite outro valor: '))

for i in range(0,QdV,1):
    x = int(input('Digite um valor: '))
    numeros.append(x)
novamente = input('Deseja realizar uma consulta (s/n): ')
while novamente == 's':    
    num = int(input('Digite um númeto para ser localizado no array: '))

    for i in range(0,QdV,1):
        if(numeros[i] == num):
           posi = i
    if (posi != -1 ):
        print('O valor foi encotrado na posição: ',posi)
    else:
        print('Valor não encontrado!')
    
    novamente = input('Deseja realizar uma nova consulta (s/n): ')
    
print("Obrigado")
