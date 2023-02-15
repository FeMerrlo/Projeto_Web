import requests

def converter(valor, moeda_destino):
    url = f'https://economia.awesomeapi.com.br/json/last/BRL-{moeda_destino}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        ask = data[f'BRL{moeda_destino}']['ask']
        return valor / float(ask)
    else:
        print(f"Erro: {response.status_code} ao acessar {url}")
        return None

valor_reais = float(input("Digite o valor em reais: "))
moeda_destino = input("Digite a moeda de destino (USD, EUR, GBP, ARS, BTC, CAD, AUD, JPY, CHF, CNY): ")

resultado = converter(valor_reais, moeda_destino.upper())

if resultado is not None:
    print(f"{valor_reais:.2f} BRL equivale a {resultado:.2f} {moeda_destino.upper()}")
