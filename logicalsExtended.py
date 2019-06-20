import cv2
img1 = cv2.imread('img1.png')
img2 = cv2.imread('img3.jpg')
rowsImg2, colsImg2, channelsImg2 = img2.shape
regionOfInterest = img1[0:rowsImg2,0:colsImg2]
#cv2.imshow('TEST',regionOfInterest)

img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray,220,255,cv2.THRESH_BINARY)
cv2.imshow('mask',mask)
inv_mask = cv2.bitwise_not(mask)


andImage = cv2.bitwise_and(regionOfInterest,regionOfInterest,mask=mask)
cv2.imshow('inv_mask',inv_mask)
cv2.imshow('gray',img2gray)
cv2.imshow('AND IMAGE',andImage)
cv2.waitKey(0) 
cv2.destroyAllWindows()
exit()