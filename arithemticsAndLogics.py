import cv2
img1 = cv2.imread('img1.png')
img2 = cv2.imread('img2.png')
add = img1 + img2
#add = cv2.add(img1,img2)
cv2.imshow("ADD",add)
cv2.waitKey(0)
cv2.destroyAllWindows()