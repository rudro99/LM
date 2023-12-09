import cv2
import matplotlib.pyplot as plt

plt.subplots_adjust(wspace=0.2, hspace=0.5)

flower = cv2.imread('flower.png')

plt.subplot(2, 3, 1)
plt.imshow(flower)
plt.title('Original Image')


rgb = cv2.cvtColor(flower, cv2.COLOR_BGR2RGB)

plt.subplot(2, 3, 2)
plt.imshow(rgb)
plt.title('RGB')


gray = cv2.cvtColor(flower, cv2.COLOR_BGR2GRAY)

plt.subplot(2, 3, 3)
plt.imshow(gray, cmap='gray')
plt.title('Gray')


edges = cv2.Canny(gray, threshold1=100, threshold2=200)

plt.subplot(2, 3, 4)
plt.imshow(edges, cmap='gray')
plt.title('Edges')

print(edges)