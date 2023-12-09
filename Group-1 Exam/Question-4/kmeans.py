import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

df = pd.read_csv('Mall_Customers.csv')

print(df)

features = df[['Annual_Income_(k$)', 'Spending_Score']]

kmeans = KMeans(n_clusters=5)  
df['Cluster'] = kmeans.fit_predict(features)

print(df)

plt.scatter(features['Annual_Income_(k$)'], features['Spending_Score'], c=df['Cluster'])