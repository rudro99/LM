import pandas as pd

df = pd.read_excel('dataset1.xlsx')

print(df)

df.to_csv('output1.csv')