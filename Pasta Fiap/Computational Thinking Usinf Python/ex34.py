from re import I
from sre_constants import RANGE


Valor1 = float(input("Entre com um valor: "))
I = 1
while (Valor1 != 5):
    print("Não pode, digite 5")
    Valor1 = float(input("Entre com 5: "))
for I in range(1,11,1):
    t = Valor1 * I
    print(f'{Valor1} X {I} = {t}')