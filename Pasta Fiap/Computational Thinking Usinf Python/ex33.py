from tokenize import String
from numpy import string_


Sexo = input("Digite o sexo (M/F): ")
while (Sexo != "M" and Sexo != "F"):
    print("Não pode, entre com M ou F")
    Sexo = input("Digite M ou F: ")
    print("Parabéns, fim do programa.")