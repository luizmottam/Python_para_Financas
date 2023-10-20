import requests
from datetime import datetime

requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,BTC-BRL")

requisicao_json = requisicao.json()
cotacao_dolar = requisicao_json["USDBRL"]["bid"]
cotacao_bitcoin = requisicao_json["BTCBRL"]["bid"]

print("Últimos valores pegos:\nDólar R${:.2f}\nBitcoin R${}".format(float(cotacao_dolar), int(cotacao_bitcoin)))