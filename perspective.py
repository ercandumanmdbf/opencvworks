import cv2
import numpy as np

img=cv2.imread("pisa.jpg")
#cv2.imshow("pisa",img)
#cv2.waitKey(0)

#now we have to learn the points for change the perspective of real img

#pt1=203,86
#pt2=408,105
#pt3=57,1023
#pt4=372,1023

pts1 = np.float32([[203,86],[408,105],[57,1023],[372,1023]])
pts2 = np.float32([[90,0],[290,0],[0,1023],[400,1023]])

M = cv2.getPerspectiveTransform(pts1,pts2)

dst = cv2.warpPerspective(img,M,(600,1024))

cv2.imshow("pisa",dst)
cv2.waitKey(0)


