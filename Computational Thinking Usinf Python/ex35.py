Valor1 = float(input("Entre com um valor: "))
I = 1
while (Valor1 <= 0):
    print("Não pode, digite um número positivo")
    Valor1 = float(input("Entre com um valor: "))
for I in range(1,11,1):
    t = Valor1 * I
    print(f'{Valor1} X {I} = {t}')