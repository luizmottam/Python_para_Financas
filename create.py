import pyodbc as py

con = py.connect(
    "Driver={SQL Server};"
    "Server=TATBITAT\MSSQLSERVER01;"
    "Database=renda;"
)
cur = con.cursor()

cur.execute('CREATE TABLE despesas(ID int IDENTITY(1,1), DESPESA float, TIPO text, DESCRIÇÃO text, DATA text)')
con.commit()

print("Criado")