A = int(input("digite o primeiro valor: "))

B = int(input("digite o segundo valor: "))

C = int(input("digite o terceiro valor: "))

if A>B>C:
    print (f"Os valores em ordem crescente são: ", A>B>C)
elif C>A>B:
    print (f"Os valores em ordem crescente são: ", C>A>B)
else:
    print (f"Os valores em ordem crescente são: ", B>A>C)