import cv2
import numpy as np


def nothing(x):
    pass
img=np.zeros((512,512,3),np.uint8)
cv2.namedWindow("Resim")
cv2.createTrackbar("R","Resim",0,255,nothing)
cv2.createTrackbar("G","Resim",0,255,nothing)
cv2.createTrackbar("B","Resim",0,255,nothing)

cv2.createTrackbar("ON/OFF","Resim",0,1,nothing)

while(1):
    cv2.imshow("Resim",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):break

    r = cv2.getTrackbarPos("R","Resim")
    g = cv2.getTrackbarPos("G","Resim")
    b = cv2.getTrackbarPos("B","Resim")
    switch = cv2.getTrackbarPos("ON/OFF","Resim") #this function is used to block the color at screen
    img[:]=[b,g,r]

    if switch==0: img[:]=[0,0,0]
    else: img[:]=[b,g,r]

cv2.destroyAllWindows()