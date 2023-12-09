import cv2
import matplotlib.pyplot as plt

plt.subplots_adjust(wspace=.5,hspace=.5)

img=cv2.imread('cafe.jpg')

plt.subplot(3,3,1)
plt.imshow(img,cmap='gray')
plt.title("Original Image")

rgb=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.subplot(3,3,2)
plt.imshow(rgb,cmap='gray')
plt.title('RGB')

gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.subplot(3,3,3)
plt.imshow(gray,cmap='gray')
plt.title('Gray')

blurred=cv2.GaussianBlur(gray, (9,9), 0)
plt.subplot(3,3,4)
plt.imshow(blurred,cmap='gray')
plt.title('Blur Picture')

edges=cv2.Canny(gray, threshold1=100, threshold2=200)
plt.subplot(3,3,5)
plt.imshow(edges,cmap='gray')
plt.title('Edges Picture')

img[255==0]=(255,0,0)
plt.subplot(3,3,6)
plt.imshow(img,cmap='gray')
plt.title('Edges Picture')

edges=edges.flatten()
print(edges)

