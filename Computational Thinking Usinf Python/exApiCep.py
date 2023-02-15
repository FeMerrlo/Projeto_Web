import requests

cep = input("Digite o CEP desejado: ")
url = f"https://viacep.com.br/ws/{cep}/json/"


response = requests.get(url)

if response.status_code == 200:
    dados = response.json()
    print(f"Logradouro: {dados['logradouro']}")
    print(f"Bairro: {dados['bairro']}")
    print(f"Cidade: {dados['localidade']}")
else:
    print("CEP não encontrado.")