import cv2
import numpy as np
from matplotlib import pyplot as plt
#sdfffffffffffffffffffffffffff
#as
#sd
#sd
#sd
img = cv2.imread('lenna.png', cv2.IMREAD_COLOR)
#HANSOL1
img = cv2.GaussianBlur(img, (5,5), 0)

edges = cv2.Canny(img,100,200)

plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('1092384019238409328409138'), plt.xticks([]), plt.yticks([])

plt.show()
