
import cv2 as cv

# hàm imread để đọc ảnh từ labtop
img = cv.imread(r'C:\Users\ngoxu\OneDrive\Pictures\HINH NEN\image (27).jpg')

# hàm imshow để hiển thị ảnh với 2 tham số truyền vào là title and img
cv.imshow("Display window", img)

# hàm waitKey để giữ ảnh không bị tắt ngay
k = cv.waitKey(0)
if k == ord("s"):
    cv.imwrite("starry_night.png", img) # hàm imwrite để lưu ảnh khi được gọi