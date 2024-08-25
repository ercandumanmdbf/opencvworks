import cv2

cam=cv2.VideoCapture(0)
fourcc=cv2.VideoWriter_fourcc(*"h264")
out=cv2.VideoWriter('output.mp4', fourcc, 20.0, (640,480))

while cam.isOpened():
    ret, frame=cam.read()
    if not ret:
        print('Failed to grab frame')
        break
    out.write(frame)
    cv2.imshow('Webcam', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print('Press q to quit')
        break