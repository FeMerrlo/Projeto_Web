N1 = int(input("Entre com o valor: "))
N2 = int(input("Entre com o outro valor: "))
while N2 < N1:
    print("O valor inicial não pode ser maior que o valor final: ")
soma = 0
for N1 in range (N1, N2 + 2,1):
    soma = soma + N1
print(f"A soma dos intervalos são: {soma}")