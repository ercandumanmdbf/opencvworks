import cv2

cam=cv2.VideoCapture(0)

if not cam.isOpened():
    print("Unable to open camera")
    exit()

while True:
    ret, frame = cam.read()
    frame=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if not ret:
        print('Failed to grab frame')
        break

    cv2.imshow('frame',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print('Press q to quit')
        break

cam.release()
cv2.destroyAllWindows()