def listar_feriados():
    print("Feriados em 2023:")
    for feriado in dados:
        data = feriado['date'].split('-')
        data_formatada = f"{data[2]}/{data[1]}/{data[0]}"
        print(f"{data_formatada} - {feriado['name']}")

def detalhar_feriado():
    data = input("Digite a data do feriado que deseja detalhar (formato: AAAA-MM-DD): ")
    for feriado in dados:
        if feriado["date"] == data:
            print(feriado["name"])
            break
    else:
        print("Feriado não encontrado.")

def criar_comentario():
    data = input("Digite a data do feriado para o qual deseja criar um comentário (formato: AAAA-MM-DD): ")
    for feriado in dados:
        if feriado["date"] == data:
            comentario = input(f"Digite um comentário para o feriado {feriado['name']}: ")
            feriado["comentario"] = comentario
            break
    else:
        print("Feriado não encontrado.")

def excluir_comentario():
    data = input("Digite a data do feriado do qual deseja excluir o comentário (formato: AAAA-MM-DD): ")
    for feriado in dados:
        if feriado["date"] == data:
            if "comentario" in feriado:
                del feriado["comentario"]
                print("Comentário excluído com sucesso.")
            else:
                print("Não há comentário para ser excluído.")
            break
    else:
        print("Feriado não encontrado.")

while True:
    print("Selecione uma opção:")
    print("1 - Exibir feriados")
    print("2 - Detalhar feriado")
    print("3 - Criar comentário para feriado")
    print("4 - Excluir comentário de feriado")
    print("5 - Sair")
    opcao = input("Opção selecionada: ")

    if opcao == "1":
        listar_feriados()
    elif opcao == "2":
        detalhar_feriado()
    elif opcao == "3":
        criar_comentario()
    elif opcao == "4":
        excluir_comentario()
    elif opcao == "5":
        break
    else:
        print("Opção inválida.")


listar_feriados()