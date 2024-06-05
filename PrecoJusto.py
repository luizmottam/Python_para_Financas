from pandas_datareader import data as pdr
from datetime import timedelta
from datetime import datetime
import yfinance as yf
import pandas as pd
import requests
import math
import time
import os

yf.pdr_override()

## 1. Criando a tabela principal
data = {'Ativo': [], 
        'Preço Atual': [], 
        'Preço Justo Ideal' : [], 
        'Preço Justo Atual' : [],
        '': [],
        'LPA': [],
        'VPA':[],
        'P/L': [],
        'P/VP': [],
       }

precos = pd.DataFrame(data)

## 2. Pega o preço atual

hoje = datetime.now()
um_ano_atras = hoje - timedelta(days = 366)

# 2.1 Indices
# papel = str(input("Nome do Papel: ")).upper()
papeis = ["ITSA4", "KLBN4", "BBAS3" , "PETR4"]

for papel in papeis:
  
  dados_mercado = pdr.get_data_yahoo(f'{papel}.SA', start= um_ano_atras, end=hoje)
  preco_atual = dados_mercado['Close'].iloc[len(dados_mercado) - 1]
  
  os.system("clear") or None
  
  ## 3. Pegando os indicativos no site fundamentus
  
  url = f'https://www.fundamentus.com.br/detalhes.php?papel={papel}'
  header = {'User-Agent' : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"}
  request = requests.get(url, headers=header)
  
  df = pd.read_html(request.text)
  
  '''
  for i, tabela in enumerate(df):
    print('---------------------------')
    print(i)
    print(tabela)  
  '''
  
  os.system('clear') or None
  df = pd.DataFrame(df[2])
  
  #O quanto você está disposto a pagar
  pl_ideal = 10 # P/L
  pvp_ideal = 1  # P/VP
  
  # O quanto o mercado está disposto a pagar agora
  pl_mercado = float(df.iloc[1, 3])/100
  pvp_mercado = float(df.iloc[2, 3])/100
  
  # Principais indices para o cálculo de peço justo Graham
  lpa = float(df.iloc[1, 5])/100
  vpa = float(df.iloc[2,5])/100
  
  ## 4. Cálculo do preço justo
  
  # Preço Justo = Raiz( Indice Graham x LPA x VPA )
  preco_justo = math.sqrt((pl_ideal * pvp_ideal) * lpa * vpa)
  preco_justo_atual = math.sqrt((pl_mercado * pvp_mercado) * lpa * vpa)
  
  ## 4. Adicionando valores a tabela principal
  if vpa > 10: 
    observacao = 'O cálculo de Graham não funciona muito bem com VPA ou LPA altos'
  else:
    observacao = ''
  precos.loc[len(precos)] = [papel, preco_atual, preco_justo, preco_justo_atual, "", lpa, vpa, pl_mercado, pvp_mercado]

print(precos)