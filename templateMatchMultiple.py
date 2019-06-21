import cv2
import numpy as np
 
 #import image
image = cv2.imread('toMatchOscar.jpg')
templateToMatch = cv2.imread('toMatchOscar.jpg',cv2.IMREAD_GRAYSCALE)


#get Width and height of template to draw a rectangle on the image
width, height = templateToMatch.shape[::-1] 

#get mask
mask = cv2.matchTemplate(image,templateToMatch,cv2.TM_CCOEFF_NORMED)

#set threshold for the match
thresholdMatch = 0.9

#get the pixels coords above specified threshold 
