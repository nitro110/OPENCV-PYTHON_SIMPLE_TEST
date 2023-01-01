import numpy as np
import cv2 as cv

# bên cạnh việc thêm 0 , 1, -1 thì ta có thể add link video vào hàm VideoCapture()
cap = cv.VideoCapture(r'D:\video_funny.mp4')

while cap.isOpened():
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow('frame', gray)

    # chỉ số trong hàm waitKey thay đổi độ nhanh hay chậm của video
    if cv.waitKey(10) == ord('q'):
        break
cap.release()
cv.destroyAllWindows()