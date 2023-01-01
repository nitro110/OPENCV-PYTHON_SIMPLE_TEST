import numpy as np
import cv2 as cv

# hàm VideoCapture() để chọn camera trên máy tính
cap = cv.VideoCapture(1)

if not cap.isOpened():
    print("Cannot open camera")
    exit()
while cap.isOpened:
    # Capture frame-by-frame ( ex 1920x1080, 640x480, 320x240 )
    ret = cap.set(cv.CAP_PROP_FRAME_WIDTH, 320)
    ret = cap.set(cv.CAP_PROP_FRAME_HEIGHT, 240)
    ret,frame = cap.read()

    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # Our operations on the frame come here ( cv.COLOR_BGR2GRAY, cv.COLOR_BGR2HSV )
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    #hsv = cv.cvtColor(frame, cv.COLOR_BRG2HSV)

    # Display the resulting frame
    cv.imshow('frame', gray)
    #cv.imshow("frame2", hsv)
    #cv.imshow("fram3", frame)
    if cv.waitKey(1) == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv.destroyAllWindows()