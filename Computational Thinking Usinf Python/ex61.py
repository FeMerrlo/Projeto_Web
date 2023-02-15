numeros = []
#for de coleta de dados
for i in range (0, 5, 1):
    num = input("Digite um número: ")
    numeros.append(num)
# Aqui vamos usar para validar se o nosso numero é maior 
for i in range (0, 5, 1):
    # esse for vai pegar e comparar com os numeros da frente para verificar se estão classicados de menor para o maior
    for j in range (i+1, 5, 1):
        #caso i que inicialmente vai estar atrás de J ser maior, ele vai trocar de posição gerando a ordenação crescente.
        if (numeros[i] < numeros[j]): # ex: se aqui i = 10 e j = 9
            aux = numeros[i] #i vira aux vira 10
            numeros[i] = numeros[j] # j vira i
            numeros[j] = aux # aux que é 10 passa na frente e vira 10
for i in range (0, 5, 1):
    print(numeros[i])