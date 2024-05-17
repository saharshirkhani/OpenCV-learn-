import numpy as np
import cv2
img = cv2.imread('AI_img.png',1)
height, width = img.shape[:2]
res = cv2.resize(img,(int(width/2), int(height/2)), interpolation = cv2.INTER_AREA)
cv2.imshow('image',res)
cv2.waitKey(0)
cv2.destroyAllWindows()