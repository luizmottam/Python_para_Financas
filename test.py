import pandas as pd

df = pd.read_csv('base.csv', sep=';', header=0, encoding = "ISO-8859-1")
oi = df.drop(['Unnamed: 4'], axis=1, inplace=True)

print(df)