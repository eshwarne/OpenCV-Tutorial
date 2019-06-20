#USE A LIBRARY CALLED Cv2 -- to do image processing
#pip install cv2, pip install numpy
#BGR -- RGB
import cv2
cap = cv2.VideoCapture(0) #0 first web came, 1 second, 2 third
while True:
	ret, frame = cap.read()
	bw = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	
	cv2.imshow("GRAY",bw)
	cv2.imshow("NAME OF THE WINDOW",frame)
	if cv2.waitKey(1) & 0xFF  == ord('q'):
		break
cap.release()
cv2.destroyAllWindows()