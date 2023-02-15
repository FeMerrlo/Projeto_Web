matriz=[]
retornar=[]
linhas = int(input('Digite a quantidade de linhas que a matriz terá: '))
while linhas > 10:
    print("O número de linhas não pode ser maior que 10, por favor digite novamente")
    linhas = int(input("Digite um novo valor: "))
colunas = int(input('Digite a quantidade de colunas que a matriz terá: '))
while colunas > 10:
    print("O número de colunas não pode ser maior que 10, por favor digite novamente")
    colunas = int(input("Digite um novo valor:"))


for l in range(0, linhas, 1):
    for c in range(0, colunas, 1):    
        num = int(input('Digite um numero: '))
        matriz[l].append(int(input("Digite um valor: ")))

for i in range(0, linhas, 1):
    print(matriz[i])

while retornar == "S":
    numero = int(input("Digite um número para ser localizado na matriz: "))


    for l in range(0, linhas, 1):
        for c in range(0, colunas, 1):
            if (matriz[l][c] == numero):
                res = res + "[" + 1 + ", " + c + "] "
                
