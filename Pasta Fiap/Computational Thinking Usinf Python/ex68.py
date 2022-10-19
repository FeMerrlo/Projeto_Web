matriz = [ [0,0,0,0], [0,0,0,0], [0,0,0,0] ]
 
for l in range(0, 3, 1):
    for c in range(0, 4, 1):
        matriz[l][c] = int(input('Digite um numero: '))
N = int(input("Digite um número para multiplicar a matriz: "))

for l in range(0, 3, 1):
    for c in range(0, 4, 1):
        r = matriz[l] [c] = matriz[l] [c] * N
for i in range (0,3,1):
    print (matriz[l])


