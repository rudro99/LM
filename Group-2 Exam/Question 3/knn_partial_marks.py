from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

X = [4, 5, 9, 4, 3, 11, 14, 8, 10, 13]
y = [21, 19, 24, 15, 16, 25, 23, 22, 21, 22]
target_classes = [0, 0, 1, 1, 0, 0, 1, 0, 1, 1]

inputData = list(zip(X,y))

print(inputData)

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(inputData, target_classes)
predict_classes = knn.predict(inputData)

accuracy = accuracy_score(target_classes, predict_classes)
print('Accuracy = ', accuracy)

x = int(input("Enter the x-value: "))
y = int(input("Enter the y-value: "))

inp = [(x, y)]

y = knn.predict(inp)
print("Result: ", y)