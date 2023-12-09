import numpy as np
from collections import Counter
from sklearn.metrics import accuracy_score

def Euclidean_distance(x1, x2):
    distance = np.sqrt((x1[0]-x2[0])**2 + (x1[1]-x2[1])**2)
    return distance

class KNN:
    def __init__(self, k=3):
        self.k = k
        
    def fit(self, X_train, Y_train):
        self.X_train = X_train
        self.Y_train = Y_train
        
    def predict(self, X_test):
        predictions = [self._predict(x) for x in X_test]
        return predictions
    
    def _predict(self, x):
        distances = [Euclidean_distance(x, x_train) for x_train in self.X_train]
        indices = np.argsort(distances)[:self.k]
        k_nearest_labels = [self.Y_train[i] for i in indices]
        most_common = Counter(k_nearest_labels).most_common(1)
        return most_common[0][0]


X = [4, 5, 9, 4, 3, 11, 14, 8, 10, 13]
y = [21, 19, 24, 15, 16, 25, 23, 22, 21, 22]
target = [0, 0, 1, 1, 0, 1, 0, 1, 1, 0]

inp = list(zip(X, y))

knn = KNN(k=5)
knn.fit(inp, target)
pred = knn.predict(inp)

accuracy = accuracy_score(target, pred)
print('Accuracy: ', accuracy)

x = int(input("Enter the x-value: "))
y = int(input("Enter the y-value: "))

inp = [(x, y)]

pre = knn.predict(inp)
print("Result: ", pred[0])