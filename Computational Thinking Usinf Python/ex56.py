name = []
age = []
for i in range (0, 100, 1):
    nome = input("Digite o nome: ")
    name.append(nome)
for i in range (0, 100, 1):
    idade = int(input("Digite a idade desta pessoa: "))
    age.append(idade)
    

print("Nome e idade: ")
for i in range(0, 100, 1):
    print("Nomes", name)
    print("Idades", age)