valor1 = int(input("digite o primeiro valor: "))

valor2 = int(input("digite o segundo valor: "))

valor3 = int(input("digite o terceiro valor: "))

if (valor1 > valor2 > valor3):
    print("O primeiro valor é o maior")

elif(valor2 > valor1 > valor3):
    print("O Segundo valor é maior")

elif(valor3 > valor2 > valor1):
    print("O Terceiro valor é maior")

else:
    print("O segundo valor é o maior")