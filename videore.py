import cv2
import time

video_object="sample_ocean.mp4"

cap=cv2.VideoCapture(video_object)

print("Width: ",cap.get(3)) #3 is for width
print("Height: ",cap.get(4)) #4 is for height

if cap.isOpened() == False:
    print("Error opening video stream or file")

while True:
    ret, frame = cap.read()

    if ret == True:
        time.sleep(0.01)
        cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Quitted from video")
        cap.release()
    else:
        break


cv2.destroyAllWindows()