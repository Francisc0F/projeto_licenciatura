import pandas as pd

df= pd.read_csv('caudal.csv', encoding= 'unicode_escape')

print(df.head())


df2 = df[['Tempo', 'Caudal']]







