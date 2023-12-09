import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

df=pd.read_csv('iris.csv')

print(df.head())

y=df['species'].values
X=df.drop(['species'],axis=1).values

le=LabelEncoder()
y=le.fit_transform(y)

X_train,X_test,y_train,y_test=train_test_split(X, y,test_size=.2,random_state=0)

model=KNeighborsClassifier(n_neighbors=3)
model.fit(X_train,y_train)
predictions=model.predict(X_test)

accuracy=accuracy_score(y_test,predictions)*100
print(accuracy)