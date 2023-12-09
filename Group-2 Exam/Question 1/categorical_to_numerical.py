import pandas as pd
from sklearn.preprocessing import LabelEncoder

df = pd.read_excel('dataset2.xlsx')

print(df)

df1 = df.copy()

le = LabelEncoder()

df1['Gender'] = le.fit_transform(df1['Gender'])
df1['Character'] = le.fit_transform(df1['Character'])

print(df1)

df2 = df.copy()

df2 = pd.get_dummies(df2, columns=['Gender', 'Character'])

print(df2.columns)

