print('Ola Mundo')
Numeros = []
#for de coleta de dados 
for i in range(1,11,1):
    x = int(input('Digite um numero: '))
    Numeros.append(x)
    #Numeros.append(int(input("Digite um numero")))
M = Numeros[0]

#Como saber o valor maior ? 
for i in range(0,10,1):
    #if  (i == 0):
        #M = Numeros[1]
    if (Numeros[i]>M):
        M = Numeros[i]
print(f"O maior array é: {M}")
