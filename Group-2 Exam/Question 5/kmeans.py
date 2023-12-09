import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score

df = pd.read_excel('dataset_kmean.xlsx')

print(df)

features = df[['X', 'Y']]

print(features)

kmeans = KMeans(n_clusters=3)

df['Clusters'] = kmeans.fit_predict(features)

print(df)

accuracy = accuracy_score(df['Target'], df['Clusters'])

print('Accuracy = ', accuracy)

x = 0.903
y = 0.601

inp = [(x, y)]

print(inp)

pred = kmeans.predict(inp)
print('Result: ', pred)
