import cv2
import matplotlib.pyplot as plt

img1=cv2.imread("img1.jpg")
img2=cv2.imread("img2.jpg")

img1=cv2.cvtColor(img1,cv2.COLOR_BGR2RGB) # convert from BGR to RGB
img2=cv2.cvtColor(img2,cv2.COLOR_BGR2RGB) # convert from BGR to RGB


plt.imshow(img1)
plt.show()

plt.imshow(img2)
plt.show()

print("Image",img1.shape,img2.shape)

img1=cv2.resize(img1,(600,600))
img2=cv2.resize(img2,(600,600))

img3=cv2.addWeighted(img1,0.5,img2,0.5,0)

plt.imshow(img3)
plt.show()
