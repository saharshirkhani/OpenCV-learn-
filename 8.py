
import cv2 
import numpy as np 
from matplotlib import pyplot as plt
  
image = cv2.imread('AI_img.png') 
  
kernel1 = np.ones((5, 5), np.float32)/30
  
img = cv2.filter2D(src=image, ddepth=-1, kernel=kernel1) 
plt.subplot(121),plt.imshow(image),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(img),plt.title('Convolved')
plt.xticks([]), plt.yticks([])
plt.show()
# cv2.imshow('Original', image) 
# cv2.imshow('Kernel Blur', img) 
cv2.waitKey() 
cv2.destroyAllWindows()