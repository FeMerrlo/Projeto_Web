
A =print("1 - Triangulo")
B =print("2 - Quadrado")
C =print("3 - Retângulo")
D =print("4 - Círculo")
E =print("5 - Fim do processo")

F =int(input("Escolha uma opção: "))
if F == 1:
    Base = float(input("Digite a base do Triangulo: "))
    Altura = float(input("Digite a altura: "))
    Area = Base*Altura/2
    print ("A area do triangulo é: ",Area)
if F == 2:
    Lado = float(input("Digite o lado do Quadrado: "))
    Area = Lado**2
    print ("A area do Quadrado é: ",Area)
if F == 3:
    Base = float(input("Digite a base do Retângulo: "))
    Altura = float(input("Digite a altura: "))
    Area = Base*Altura
    print ("A area do Retângulo é: ",Area)
if F == 4:
    Raio = float(input("Digite o Raio do circulo: "))
    Area = 3.14 * Raio
    print ("A area do Retângulo é: ",Area)
if F == 5:
    print ("Fechando o progama ")
else:
    F  =int(input("Você digitou um número errado, digite umas das opções acima: "))

