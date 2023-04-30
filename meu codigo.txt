import email
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
from datetime import timedelta
from pandas_datareader import data as pdr
from gtts import gTTS
from playsound import playsound
import time
indices = ['HGLG11.SA', 'DEVA11.SA', 'MXRF11.SA', 'BRL=X']

hoje = datetime.now()
um_ano_atras = hoje - timedelta(days = 366)
dados_mercado = pdr.get_data_yahoo(indices, start= um_ano_atras, end=hoje)

dados_fechamento = dados_mercado['Adj Close']
dados_fechamento.columns = ["HGLG11", "DEVA11", "MXRF11", "USD/BRL"]
dados_fechamento = dados_fechamento.dropna()

# Enviando email
host = "smtp.gmail.com"
port = "587"
login = "luidimotta29@gmail.com"
senha = "qckzzsqgpijruhtj"

server = smtplib.SMTP(host, port)

server.ehlo()
server.starttls()
server.login(login, senha)

corpo = f"""
HGLG11  R${dados_fechamento.iloc[0,0]:.2f}
DEVA11  R${dados_fechamento.iloc[0,1]:.2f}
MXRF11  R${dados_fechamento.iloc[0,2]:.2f}
USD/BRL R${dados_fechamento.iloc[0,3]:.2f}

Abs, Alice
"""


email_smg = MIMEMultipart()
email_smg['From'] = login
email_smg['To'] = login
email_smg['Subject'] = "Preço de ATIVOS, para ficar de olho!"
email_smg.attach(MIMEText(corpo, 'plain'))

server.sendmail(email_smg['From'], email_smg['To'], email_smg.as_string())
server.quit()