import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread("nike.jpeg",0)
plt.figure()
plt.imshow(img,cmap="gray")
plt.axis("off")
plt.title("Nike Original")
plt.show()

#erosion
kernel=np.ones((5,5),np.uint8)
erosion=cv2.erode(img,kernel,iterations=1)
plt.figure()
plt.imshow(erosion,cmap="gray")
plt.axis("off")
plt.title("Erosion")
plt.show()


#dilation
dilation=cv2.dilate(img,kernel,iterations=1)
plt.figure()
plt.imshow(dilation,cmap="gray")
plt.axis("off")
plt.title("Dilation")
plt.show()

#add white noise
noise=np.random.randint(0,2,size=img.shape[:2])
noise=noise*255
noisy_img=img+noise
plt.figure()
plt.imshow(noisy_img, cmap="gray")
plt.axis("off")
plt.title("Noisy Image")
plt.show()

#opening
opening=cv2.morphologyEx(noisy_img.astype(np.float32),cv2.MORPH_OPEN,kernel)
plt.figure()
plt.imshow(opening, cmap="gray")
plt.axis("off")
plt.title("Opening")
plt.show()

#add black noise
black_noise=np.random.randint(0,2,size=img.shape[:2])*-255
noisy_img=img+black_noise
plt.figure()
plt.imshow(noisy_img, cmap="gray")
plt.axis("off")
plt.title("Black Noisy Image")
plt.show()

#closing
closing=cv2.morphologyEx(noisy_img.astype(np.float32),cv2.MORPH_CLOSE,kernel)
plt.figure()
plt.imshow(closing, cmap="gray")
plt.axis("off")
plt.title("Closing")
plt.show()

#gradient
gradient=cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel)
plt.figure()
plt.imshow(gradient, cmap="gray")
plt.axis("off")
plt.title("Gradient")
plt.show()