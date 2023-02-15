from re import A


b = float(input("Digite o valor da base = "))

h = float(input("Digite o valor da altura = "))

A = b*h

if (A > 100):
    print ("Seu terreno é grande")
else:
    print ("o tamanho do seu terreno é:",A,"Metros")