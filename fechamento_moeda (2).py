import requests
from datetime import datetime

requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,BTC-BRL")

requisicao_json = requisicao.json()
cotacao_dolar = requisicao_json["USDBRL"]["bid"]
cotacao_bitcoin = requisicao_json["BTCBRL"]["bid"]

print("Últimos valores pegos:\nDólar R${:.2f}\nBitcoin R${}".format(float(cotacao_dolar), int(cotacao_bitcoin)))


datas_anteriores = requests.get("https://economia.awesomeapi.com.br/json/daily/USD-BRL/15")
datas_anteriores_jason = datas_anteriores.json()

print(datas_anteriores_jason)