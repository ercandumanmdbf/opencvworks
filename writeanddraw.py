import cv2
import numpy as np

#create full black image
img=np.zeros((512,512,3),np.uint8)

#draw line
cv2.line(img,(0,0),(511,511),(255,0,0),5)

#draw rectangle and square
cv2.rectangle(img,(384,0),(510,128),(0,255,0), -1) #write cv2.FILLED or -1 to fill inside

#draw circle
cv2.circle(img,(447,63),63,(0,0,255),-1)

#put text
cv2.putText(img,"TEXT",(10,500),cv2.FONT_HERSHEY_COMPLEX_SMALL,4,(255,255,255),2)

cv2.imshow("resim",img)
cv2.waitKey(0)
cv2.destroyAllWindows()