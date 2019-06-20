import cv2
img  = cv2.imread('checks.jpg')
scale_percent = 30 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
# resize image
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
gray = cv2.cvtColor(resized,cv2.COLOR_BGR2GRAY)
ret,threshold = cv2.threshold(gray,11,255,cv2.THRESH_BINARY)
guasThreshold = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)
cv2.imshow('ORIGINAL',resized)
cv2.imshow('thres',guasThreshold)
cv2.waitKey(0)
cv2.destroyAllWindows()