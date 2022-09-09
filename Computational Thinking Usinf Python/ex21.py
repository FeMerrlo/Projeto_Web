
valor1 = int(input("digite o primeiro valor: "))

valor2 = int(input("digite o segundo valor: "))

A =print("1 - Multiplicação")
B =print("2 - Adição")
C =print("3 - Divisão")
D =print("4 - Subtração")
E =print("5 - Fim do processo")

F =int(input("Escolha uma opção: "))
if F == 1:
    A = valor1*valor2
    print ("O Resultado é: ",A)
if F == 2:
    B = valor1+valor2
    print ("O Resultado é: ",B)

if F == 3: 
  if valor1 and valor2 == 0:
    print ("Falha na Matrix, Digite um denominador maior que zero")
    valor1 = int(input("digite o primeiro valor: "))

    valor2 = int(input("digite o segundo valor: "))
  elif valor1 and valor2 != 0:
    C = valor1/valor2
    print ("O Resultado é: ",C)
        
if F == 4:
    D = valor1-valor2
    print ("O Resultado é: ",D)
if F == 5:
    print ("Fechando o progama ")
else:
    F=int(input("Você digitou um número errado, digite umas das opções acima: "))

