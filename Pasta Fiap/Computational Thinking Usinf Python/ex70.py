matriz=[]
 
linhas = int(input('Digite a quantidade de linhas que a matriz terá: '))
while linhas > 10:
    print("O número de linhas não pode ser maior que 10, por favor digite novamente")
    linhas = int(input("Digite um novo valor: "))
colunas = int(input('Digite a quantidade de colunas que a matriz terá: '))
while colunas > 10:
    print("O número de colunas não pode ser maior que 10, por favor digite novamente")
    colunas = int(input("Digite um novo valor:"))

for i in range(0, linhas, 1):
    matriz.append([])
for l in range(0, linhas, 1):
    for c in range(0, colunas, 1):    
        num = int(input('Digite um numero: '))
        matriz[l].append(num)
print(matriz)

for l in range(0, linhas, 1):
    for c in range(0, colunas, 1): 
      p = int(input("Deseja consultar alguma posição da matriz: "))
      
