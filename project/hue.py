import cv2
import numpy as np
image = cv2.imread('input.jpg')
hsv_image=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
cv2.imshow('orginal image',image)
cv2.imshow('HSV image',hsv_image)
cv2.imshow('HUE channel',hsv_image[:,:,0])
cv2.imshow('Saturation channel',hsv_image[:,:,1])
cv2.imshow('value channel',hsv_image[:,:,2])
cv2.waitKey()
cv2.destroyAllWindows()
