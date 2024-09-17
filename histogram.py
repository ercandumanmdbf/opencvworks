import cv2
import matplotlib.pyplot as plt
import numpy as np

img=cv2.imread("redblue.png")
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.figure()
plt.imshow(img)
plt.axis("off")
plt.title("Original Image")
plt.show()

hist=cv2.calcHist([img],[0],None,[256],[0,256])
plt.figure()
plt.plot(hist)
plt.title("Histogram for Blue and Red")
plt.show()

color=('b','g','r')
for i,col in enumerate(color):
    histr=cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(histr,color=col)


img_flower=cv2.imread("img2.jpg")
img_flower=cv2.cvtColor(img_flower,cv2.COLOR_BGR2RGB)
plt.figure()
plt.imshow(img_flower)
plt.axis("off")
plt.title("Original Image")
plt.show()

hist_flower=cv2.calcHist([img_flower],[0],None,[256],[0,256])
plt.figure()
plt.plot(hist_flower)
plt.title("Histogram for Flower")
plt.show()

for i,col in enumerate(color):
    histr_flower=cv2.calcHist([img_flower],[i],None,[256],[0,256])
    plt.plot(histr_flower,color=col)
    plt.show()


img_drop=cv2.imread("img1.jpg",0)
plt.figure()
plt.imshow(img_drop, cmap="gray")


hist_drop=cv2.calcHist([img_drop],[0],None,[256],[0,256])
plt.figure()
plt.plot(hist_drop)
plt.show()

#more contrast
eq_hist=cv2.equalizeHist(img_drop)
plt.figure()
plt.imshow(eq_hist, cmap="gray")
plt.show()

