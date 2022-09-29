from this import d


N1 = int(input("Entre com o valor: "))
N2 = int(input("Entre com o outro valor: "))
while (N1 <= 0):
    print("Não pode, digite um número positivo")
    N1 = int(input("Entre com um valor: "))
while (N2 <= 0):
    print("Não pode, digite um número positivo")
    N2 = int(input("Entre com um valor: "))
for N1 in range (N1, N2 + 1,1):
    if N1 >= 10:
        if N1 / 2 == 0:
         print("Programa Encerrado")