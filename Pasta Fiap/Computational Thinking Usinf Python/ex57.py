#Armazenar o nome, sexo e idade de cem pessoas.
#entradas no sentido de aceitar apenas “F” ou “M” 
#para o sexo e valores positivos para a idade.
#Após a digitação dos dados, exibir os dados (nome, sexo e idade)

name = []
age = []
sex = []

for i in range (0, 2, 1):
    nome = input("Digite o nome: ")
    name.append(nome)
    idade = int(input("Digite a idade: "))
    age.append(idade)
    while idade < 0:
        print("Não aceitamos menores de 0 anos: ")
        idade = int(input("Digite uma nova idade: "))
    sexo = input("Digite o nome: 'M/F' ")
    while sexo != "M" and sexo != "F":
        print("Não aceitamos opções diferentes de 'M' ou 'F'")
        sexo = input("Digite 'M' ou 'F': ")
    sex.append(sexo)

while sex == "F":
    for i in range (0, 2, 1):
      print("Nome, Idade e Sexo das Mulheres : ")
      print(F"{idade[i]}")
      print("Nomes", name)
      print("Idades", age)
      print("Sexo", sex)

print("Acabou")

