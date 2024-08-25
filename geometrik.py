import cv2
import numpy as np

img=np.zeros((512,512,3),np.uint8)

#cv2.line(img,(0,0),(511,511),(240,0,3),thickness=8)
#cv2.putText(img,"Merhaba",(10,500),cv2.FONT_HERSHEY_COMPLEX_SMALL,4,(255,255,255),2)
#cv2.circle(img,(47,47),(4),(240,255,0),3)
#cv2.circle(img,(85,85),(4),(240,255,0),3)
#cv2.circle(img,(110,110),(4),(240,255,0),3)
#cv2.rectangle(img,(255,255),(200,200),(240,255,0),3)
#cv2.ellipse(img,(300,300),(100,50),0,0,180,(240,255,0),3)
#cv2.rectangle(img,(355,255),(200,200),(240,255,0),3)

dots=np.array([[100,100],[150,150],[423,111]])
cv2.polylines(img,[dots],True,(240,255,0),3)

cv2.imshow("resim", img)
cv2.waitKey(0)
cv2.destroyAllWindows()