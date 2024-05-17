import cv2 
import numpy 

def nothing(x): 
	pass

img = numpy.zeros((300, 512, 3), numpy.uint8) 
cv2.namedWindow('image') 

cv2.createTrackbar('R', 'image', 0, 255, nothing) 

cv2.createTrackbar('G', 'image', 0, 255, nothing) 

cv2.createTrackbar('B', 'image', 0, 255, nothing) 

while(True): 
	cv2.imshow('image', img) 

	k = cv2.waitKey(1) & 0xFF
	if k == 27: 
		break

	r = cv2.getTrackbarPos('R', 'image') 
	g = cv2.getTrackbarPos('G', 'image') 
	b = cv2.getTrackbarPos('B', 'image') 

	img[:] = [b, g, r] 

cv2.destroyAllWindows() 
