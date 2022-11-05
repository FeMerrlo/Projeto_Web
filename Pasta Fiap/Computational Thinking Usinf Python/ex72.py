mm = []
mt = []
mn = []

fileiras = int(input("Quantas fileiras a casa de show terá??"))
cadeiras = int(input("Quantas cadeiras a casa de show terá??"))



# Cria as linhas na Matriz
for i in range(0, 10, 1):
    busao.append([])
 
# Cria para cada linha, cria as colunas na Matriz já gravando o valor digitado
for l in range(0, 10, 1):
    for c in range(0, 4, 1):      
        busao[l].append("-----")

for l in range(0, 10, 1):
    print(busao[l])

while(retornar=="s"):
    nome = input("Digite o nome do viajante (até 5 caracteres):  ")
    fileira = int(input("Digite a fileira que você deseja sentar (1 a 10")) -1
    cadeira = int(input("Digite a cadeira que você deseja semtar (1 a 4)")) -1

    if (busao[fileira][cadeira] =="-----"):
        busao [fileira][cadeira] == nome
        print("reserva feita com sucesso")
    else:
        print("Esse assento já esta reservado! ")
    
    retornar = input("Deseja realizar mais alguma resrva ? S/N")

print("Mapa das reservas do Ônibus: ")
