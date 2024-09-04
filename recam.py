import cv2

cap=cv2.VideoCapture(0)

width=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

print("Capture",width,height)

writer=cv2.VideoWriter("output.mp4",cv2.VideoWriter_fourcc(*"DIVX"),20.0,(width,height))

while True:
    ret,frame=cap.read()
    cv2.imshow("frame",frame)
    if ret==True:
        writer.write(frame)
    else:
        break

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
writer.release()
cv2.destroyAllWindows()

print("Video saved successfully.")
cv2.destroyAllWindows()