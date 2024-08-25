import cv2

cam=cv2.VideoCapture("videoSample.mp4")

if not cam.isOpened():
    print("Unable to open camera")
    exit()

while True:
    ret, frame = cam.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if not ret:
        print('Failed to grab frame')
        break
    cv2.imshow('VR Kids',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print('Quitted from video')
        break

cam.release()
cv2.destroyAllWindows()