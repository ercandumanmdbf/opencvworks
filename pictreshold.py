import cv2
import matplotlib.pyplot as plt

img=cv2.imread("img2.jpg")
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
plt.figure()
plt.imshow(img, cmap='gray')
plt.axis("off")
plt.show()

#Thresholding
threshold=125
th, thresh_img=cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY)
plt.figure()
plt.imshow(thresh_img, cmap='gray')
plt.axis("off")
plt.show()

#adaptive threshold
adaptive_thresh_img=cv2.adaptiveThreshold(img, 255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,8)
plt.figure()
plt.imshow(adaptive_thresh_img, cmap='gray')
plt.axis("off")
plt.show()