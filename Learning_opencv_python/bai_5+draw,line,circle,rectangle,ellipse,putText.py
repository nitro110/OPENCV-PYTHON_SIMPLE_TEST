import numpy as np
import cv2 as cv
# Create a black image
img = np.zeros((512,512,3), np.uint8)
# Draw a diagonal blue line with thickness of 5 px
# ham vẽ đường thẳng cv.line() ( để vẽ đường thẳng ta cần tọa độ điểm bắt đầu và điểm kết thúc )
cv.line(img,(0,0),(511,511),(255,0,0),5)

# hàm vẽ hình chữ nhật cv.rectangle() ( để vẽ hình chữ nhật ta cần tọa độ góc phía trên bên trái và tọa độ điểm góc phía dưới bên phải )
cv.rectangle(img,(384,0),(510,128),(0,255,0),3)

# hàm vẽ hình tròn cv.circle() ( để vẽ hình tròn ta cần tọa độ tâm hình hình tròn + bán kính )
cv.circle(img,(447,63), 63, (0,0,255), -1)

# hàm vẽ hình ellipse()
cv.ellipse (img,(256,256),(100,50),0,0,180,255,-1)

# hàm vẽ đa giác cv.polylines()
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
cv.polylines (img,[pts], True ,(0,255,255))

# hàm thêm văn bản vào hình ảnh cv.putText()
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv.LINE_AA)

cv.waitKey(0)