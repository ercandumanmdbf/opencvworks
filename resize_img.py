import cv2

img=cv2.imread("sample_mimi.jpg")
print("Pic Size:",img.size,img.shape)

img_resize=cv2.resize(img,(300,300))

cv2.imshow("Mimi",img)
cv2.imshow("Mimi Resize",img_resize)

print("Resized Image",img_resize.size,img_resize.shape)

#img crop
cropped_img=img_resize[100:200,30:200]
cv2.imshow("Cropped Mimi",cropped_img)

cv2.waitKey(0)
cv2.destroyAllWindows()