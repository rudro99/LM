import pandas as pd
data={
      'Name':['Mahfuz','AKM','Limon','Rahman'],
      'Age':[23,34,56,78],
      'City':['A','B','C','D']
      }
df=pd.DataFrame.from_dict(data)

df.to_csv("Bal.csv")
df.to_excel("Bal.xlsx")

df=pd.read_csv("Bal.csv")
print(df)
df=pd.read_excel("Bal.xlsx")
print(df)