from re import L


N = float(input("Digite um valor N: "))
while (N > 50):
    print("Não será permitido valor maior que 50")
    N = float(input("Entre com um valor N: "))
    while (N < 0):
     print("Não será permitido valor negativo")
     N = float(input("Entre com um valor N: "))
while (N < 0):
    print("Não será permitido valor negativo")
    N = float(input("Entre com um valor N: "))
    while (N > 50):
     print("Não será permitido valor maior que 50")
     N = float(input("Entre com um valor N: "))
#Valor de cima 
VDC = 1 
#Valor de baixo
VDB = 2
L = 1
while (L <= N):
    print(f'{VDC}\n--\n{VDB} \n')
    VDC = VDC + 1
    VDB = VDB + 1
    L = L + 1
