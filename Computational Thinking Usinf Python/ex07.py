from ast import If
from http.client import ImproperConnectionState
from re import A


P = float(input("Digite seu peso: "))

A = float(input("Digite sua altura: "))

IMC = P/(A*A)
if (IMC > 25):
    print ("Você esta acima do peso ideal")
else:
    print ("Você esta no peso ideal")