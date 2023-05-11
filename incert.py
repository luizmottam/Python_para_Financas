import pyodbc as py
import pandas as pd

#df = pd.read_excel('mesess.xlsx')
df = pd.read_excel('2022.xlsx')
con = py.connect(
    "Driver={SQL Server};"
    "Server=LAPTOP-9EIPUPNB\MSSQLSERVER01;"
    "Database=renda;"
)

cur = con.cursor()
linhas = len(df.index)
print(linhas)
x = 0

'''while x < linhas:
    mes = df.loc[x, 'MÊS']
    ano = df.loc[x, 'ANO']
    salario = df.loc[x, 'SALARIO']
    sql_insert = f"INSERT INTO meses(MÊS, ANO, SALARIO) values('{mes}',{ano},{salario})"
    con.execute(sql_insert)
    cur.commit()
    x+=1'''

'''while x < linhas:
    mes = df.loc[x, 'Meses']
    du = df.loc[x, 'Dias Úteis']
    ps = df.loc[x, 'Previsão Salarial']
    hs = df.loc[x, 'Histórico Salário']
    dp = df.loc[x, 'Diferença Porcentual']
    sql_insert = f"insert into Ano2022(Meses, Dias_Úteis, Previsão_Salarial, Histórico_Salário, Diferença_Porcentual) values('{mes}',{du}, {ps}, {hs}, '{dp}')"    
    con.execute(sql_insert)
    cur.commit()

    x += 1'''
    
print("Concluido")