
"""
Spyder Editor

This is a temporary script file.
"""

import cv2
from matplotlib import pyplot as plt



resim = cv2.imread("resim1.webp",0)

cv2.imshow("resim", resim)
cv2.waitKey(3)
plt.imshow(resim,cmap="grey")
plt.show()

