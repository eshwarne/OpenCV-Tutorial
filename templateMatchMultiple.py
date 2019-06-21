import cv2
import numpy as np
 
 #import image
image = cv2.imread('img3.jpg')
imageGray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
templateToMatch = cv2.imread('toMatchOscar.jpg',cv2.IMREAD_GRAYSCALE)


#get Width and height of template to draw a rectangle on the image
width, height = templateToMatch.shape[::-1] 

#get mask
mask = cv2.matchTemplate(imageGray,templateToMatch,cv2.TM_CCOEFF_NORMED)

#set threshold for the match
thresholdMatch = 0.5

#get the pixels coords above specified threshold 
locationOfMatch = np.where(mask>=thresholdMatch)

#draw the rectangle on the image
for point in zip(*locationOfMatch[::-1]):
    cv2.rectangle(image,point,(point[0]+width,point[1]+height),(255,100,100),3)

cv2.imshow('detection of temp',image)
cv2.waitKey(0)
cv2.destroyAllWindows()