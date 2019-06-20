import cv2
capture = cv2.VideoCapture(0)
while True:
    _, frame = capture.read()
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    res = cv2.bitwise_and(hsv,hsv)
    median = cv2.medianBlur(res,15)
    cv2.imshow('NEW',median)
    if(cv2.waitKey(1) & 0xFF == ord('q') ):
        break

cv2.destroyAllWindows()