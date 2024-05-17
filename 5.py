import cv2 as cv
import numpy as np
img1 = cv.imread('AI_img.png')
img2 = cv.imread('whitelog.png')
rows,cols,channels = img2.shape
roi = img1[0:rows, 0:cols]
img2gray = cv.cvtColor(img2,cv.COLOR_BGR2GRAY)
ret, mask = cv.threshold(img2gray, 10, 255, cv.THRESH_BINARY)
mask_inv = cv.bitwise_not(mask)
img1_bg = cv.bitwise_and(roi,roi,mask = mask_inv)
img2_fg = cv.bitwise_and(img2,img2,mask = mask)
dst = cv.add(img2_fg, img1_bg)
img1[0:rows, 0:cols ] = dst
cv.imshow('image',img1)
cv.waitKey(0)
cv.destroyAllWindows()