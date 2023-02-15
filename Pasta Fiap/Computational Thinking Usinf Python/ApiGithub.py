import requests


login = input("Digite o Login do GitHub: ")
url = f"https://api.github.com/users/joseffe10"


response = requests.get(url)


if response.status_code == 200:
    dados = response.json()
    print(f"CEP: {dados['cep']}")
    print(f"Logradouro: {dados['logradouro']}")
    print(f"Bairro: {dados['bairro']}")
    print(f"Cidade: {dados['localidade']}")
    print(f"Estado: {dados['uf']}")
else:
    print("CEP não encontrado.")