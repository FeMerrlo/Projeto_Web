from ast import If
from re import I


A = int(input("digite o primeiro valor: "))

B = int(input("digite o segundo valor: "))

C = int(input("digite o terceiro valor: "))

if A+B<C:
    print (f"Soma de A+B: {A+B: .0f} é menor que C")