import pyodbc as py
import pandas as pd
import os
import time

os.system('cls') or None
print("Contectando-se ao servidor...")
#Conecta ao servidor
con = py.connect(
    "Driver={SQL Server};"
    "Server=TATBITAT;"
    "Database=Dados;"
)
os.system('cls') or None
time.sleep(3)
print("Coneção bem sucedida!")
time.sleep(2)
os.system('cls') or None
cur = con.cursor()



# LEITOR
tabela = pd.read_sql('select * from Doencas', con)
linhas = len(tabela.index)


# Lista igual
x = 0
todos_sintomas = []

# O while percorre toda a coluna Sintomas
while x < linhas:
    sintomas = tabela.loc[x, 'Sintomas']
    doenca = tabela.loc[x, 'Doenca']

    sintoma = sintomas.split(", ") #separa os sintomas de cada linha por "," 
    
    # O for vai adicionar todos os sintomas a lista todos_sintomas
    for sintoma1 in sintoma:
        todos_sintomas.append(sintoma1) # Adiciona todos os sintomas em uma lista

    x += 1 

valores = []
repetidos = set()

for dado in todos_sintomas:
    if dado not in valores:
        valores.append(dado) # Confirma a lista todos_sintomas
    else:
        repetidos.add(dado) # bota os valores já repetidos em um conjunto

repetidos = list(repetidos)
print(len(valores))
'''x = 0
y = 0
oi = 0
while x < linhas:
    sintomas = tabela.loc[x, 'Sintomas']
    doenca = tabela.loc[x, 'Doenca']

    sintoma = sintomas.split(", ") #separa os sintomas de cada linha por "," 
    while y < len(sintoma):
        print(sintoma[y])
        print(repetidos[x])
        time.sleep(5)
        os.system('cls') or None
        if(sintoma[y] == repetidos[x]):
            print
        y += 1

    x += 1 '''