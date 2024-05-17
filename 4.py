import numpy as np
import cv2
import matplotlib.pyplot as plt
img = cv2.imread('OpenCV_Python.png',0)
for i in range(100):
   for j in range(100):
      img[i,j]=[0,0,0]
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()