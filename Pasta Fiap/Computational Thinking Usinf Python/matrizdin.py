matriz=[]
 
linhas = int(input('Digite a quantidade de linhas que a matriz terá: '))
colunas = int(input('Digite a quantidade de colunas que a matriz terá: '))
 
# Cria as linhas na Matriz
for i in range(0, linhas, 1):
    matriz.append([])
 
# Cria para cada linha, cria as colunas na Matriz já gravando o valor digitado
for l in range(0, linhas, 1):
    for c in range(0, colunas, 1):    
        num = int(input('Digite um numero: '))
        matriz[l].append(num)
 
# Mostra a matriz um uma linha única
print(matriz)
 
# Mostra a matriz de forma real
for i in range(0, linhas, 1):
    print(matriz[i])
 
# Mostra a matriz de forma real
for l in range(0, linhas, 1):
    for c in range(0, colunas, 1):
        print(matriz[l][c])
