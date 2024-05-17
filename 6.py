import numpy as np 
import cv2 
img = cv2.imread('AI_img.png',1) 
cv2.line(img,(20,400),(400,20),(255,255,255),3) 
cv2.rectangle(img,(200,100),(400,400),(0,255,0),5) 
cv2.circle(img,(80,80), 55, (255,255,0), -1) 
cv2.ellipse(img, (300,425), (80, 20), 5, 0, 360, (0,0,255), -1) 
cv2.imshow('image',img) 
cv2.waitKey(0) 
cv2.destroyAllWindows() 
