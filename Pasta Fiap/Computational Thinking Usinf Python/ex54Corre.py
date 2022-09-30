numeros = []
resultado = []

for i in range(0, 20, 1):
    num = int(input("Digite um valor: "))
    numeros.append(num)

const = int(input("Digite um valor para a constante: "))

for i in range(0, 20, 1):
    resultado.append(const * numeros[i])

print("Resultados: ")
for i in range(0, 20, 1):
    print(numeros[i])
    print(resultado[i])