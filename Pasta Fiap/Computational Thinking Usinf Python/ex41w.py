N = float(input("Digite um valor N: "))
while (N > 100):
    print("Não será permitido valor maior que 100")
    N = float(input("Entre com um valor N: "))
    while (N < 0):
     print("Não será permitido valor negativo")
     N = float(input("Entre com um valor N: "))
while (N < 0):
    print("Não será permitido valor negativo")
    N = float(input("Entre com um valor N: "))
    while (N > 100):
     print("Não será permitido valor maior que 100")
     N = float(input("Entre com um valor N: "))
#SNI = soma de n impares
SNI = 3
#SDR = soma de Resultados
SDR = 2
#L = Resultado
L = 1
while (N >= L):
    R = SNI + SDR
    print(f'{SNI} + {SDR} = {R}')
    SNI = SNI + 2
    SDR = R
    L = L + 1

# 
