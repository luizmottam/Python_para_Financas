import pyodbc as py
import pandas as pd
import os
import time

os.system('cls') or None

print("Contectando-se ao servidor...")

#Le a planilha
df = pd.read_csv('base.csv', sep=';', header=0, encoding = "ISO-8859-1")
linhas = len(df.index)

#Conecta ao servidor
con = py.connect(
    "Driver={SQL Server};"
    "Server=TATBITAT\MSSQLSERVER01;"
    "Database=renda;"
)

os.system('cls') or None
time.sleep(3)
print("Coneção bem sucedida!")
time.sleep(2)
os.system('cls') or None
cur = con.cursor()
oi = df.drop(['Unnamed: 4'], axis=1, inplace=True)

x = 0
while x < linhas:
    despesa = df.loc[x , 'DESPESA']
    tipo = df.loc[x , 'TIPO']
    descricao = df.loc[x , 'DESCRIÇÃO']
    dataa = df.loc[x , 'DATAA']
    x += 1

    sql_insert = sql_insert = f"INSERT INTO despesas(DESPESA, TIPO, DESCRIÇÃO, DATA) VALUES({despesa}, '{tipo}', '{descricao}', '{dataa}')"
    cur.execute(sql_insert)
    con.commit()

print("Dados inseridos com sucesso!")
time.sleep(3)
os.system('cls') or None