
ValorX = int(input("Entre com um valor X: "))
while (ValorX <= 0):
    print("Não pode, digite um número positivo")
    ValorX = int(input("Entre com um valor: "))

Intervalo = int(input("Entre com o valor do intervalo: "))
while (Intervalo > ValorX):
    print("Não pode, digite um valor maior que: ")
    Intervalo = int(input("Entre com um valor:"))
while (Intervalo <= ValorX):
    r = ValorX * Intervalo
    print(f'{ValorX} X {Intervalo} = {r}')
    Intervalo = Intervalo + 1

#I = float(input("Informe um i"))