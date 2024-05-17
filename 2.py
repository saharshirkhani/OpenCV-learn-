import numpy as np
import cv2
img = cv2.imread('AI_img.png',0)
cv2.imshow('image',img)
key=cv2.waitKey(0)
if key==ord('s'):
   cv2.imwrite("AI_img_GS.png", img)
cv2.destroyAllWindows()