import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler

df=pd.read_csv("live.csv")
print(df.head())

df.drop(['Column1','Column2','Column3','Column4','status_id','status_published'],axis=1,inplace=True)
print(df)

df=df.dropna()

X=df
y=df['status_type']

le=LabelEncoder()
X['status_type']=le.fit_transform(X['status_type'])
y=le.transform(y)

ms=MinMaxScaler()
X=ms.fit_transform(X)

print(df.head())


