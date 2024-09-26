print('Ola Mundo')
Numeros = []
#for de coleta de dados 
for i in range(1,21,1):
    #x = int(input('Digite um numero: '))
    #Numeros.append(x)
    Numeros.append(int(input("Digite um numero: ")))
const = int(input("Digite um valor para a constante: "))
# aqui nós  varremos o array novamente para fazer a multiplicação
for i in range(0,20,1):
    Numeros[i] = Numeros[i] * const #aqui ele faz a operação de multiplicação em toda a array
    print(Numeros[i])
