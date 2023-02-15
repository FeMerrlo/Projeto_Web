name = []
rm = []
curso= []

for i in range (0, 5, 1):
    nome = input("Digite o nome: ")
    name.append(nome)
for i in range (0, 5, 1):
    RM = int(input("Digite o RM desta pessoa: "))
    rm.append(RM)
    
for i in range (0, 5, 1):
    Cursos =(input("Digite o Curso desta pessoa: "))
    curso.append(Cursos)    
    

print("Nome RM e Curso: ")
for i in range(0, 5, 1):
    print("Nomes", name)
    print("RMs", rm)
    print("Cursos", curso)