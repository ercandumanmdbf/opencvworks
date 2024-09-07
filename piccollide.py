import cv2
import numpy as np

img=cv2.imread("sample_mimi.jpg") #original image object
#cv2.imshow("original",img)
#cv2.waitKey(0)

hor=np.hstack((img,img)) #object add picture horizontally
#cv2.imshow("horizontal",hor)
#cv2.waitKey(0)

ver=np.vstack((img,img)) #object add picture vertically
cv2.imshow("vertical",ver)
cv2.waitKey(0)


cv2.destroyAllWindows()