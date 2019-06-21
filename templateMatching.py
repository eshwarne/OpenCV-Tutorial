#Template matching is given an template image or many, we try to match the exact template in an image to capture that template in the match
#CONS : This is not similiar to face and object reocgintion, it is more of finding the coccurence of one image in another image with the same semantics
#The rotation of the image should also be the same. For example, taking a water bottles image and matching it with a flipped water bottle won't work

import cv2
import numpy as np
img =  cv2.imread('templateMatchingTut.jpg')
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgTemplate  = cv2.imread('templateToMatch.jpg',cv2.IMREAD_GRAYSCALE)
windowName = cv2.namedWindow('DISPLAY OF MATCH')
#Here we have to reverse the array as arrays return row and column pos which is the opposite of x and y coords. ROWS --> Y, COLS --> X
width, height = imgTemplate.shape[::-1]



mask = cv2.matchTemplate(imgGray,imgTemplate,cv2.TM_CCOEFF_NORMED)
# mask = cv2.matchTemplate(imgGray,imgTemplate,cv2.TM_CCORR)
# mask = cv2.matchTemplate(imgGray,imgTemplate,cv2.TM_CCOEFF)
# mask = cv2.matchTemplate(imgGray,imgTemplate,cv2.TM_CCORR_NORMED)
thresholdMatch = 0.99
locationOfMatch = np.where(mask>=thresholdMatch)

for pointOfMatch in zip(*locationOfMatch[::-1]):
    cv2.rectangle(img,pointOfMatch,(pointOfMatch[0]+width,pointOfMatch[1]+width),(255,0,0),3)

cv2.imshow(windowName, mask)
cv2.imshow(windowName,img)

cv2.waitKey(0)
cv2.destroyAllWindows()