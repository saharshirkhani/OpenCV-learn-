import numpy as np
import cv2 as cv

cap = cv.VideoCapture('traffic.mp4')

ret,frame = cap.read()

x, y, w, h = 300, 200, 100, 50
tracker = (x, y, w, h)

region = frame[y:y+h, x:x+w]
hsv_reg = cv.cvtColor(region, cv.COLOR_BGR2HSV)
mask = cv.inRange(hsv_reg, np.array((0., 60.,32.)), np.array((180.,255.,255.)))
reg_hist = cv.calcHist([hsv_reg],[0],mask,[180],[0,180])
cv.normalize(reg_hist,reg_hist,0,255,cv.NORM_MINMAX)

criteria = ( cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 1 )

while(1):
   ret, frame = cap.read()

   if ret == True:
      hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
      dst = cv.calcBackProject([hsv],[0],reg_hist,[0,180],1)

      ret, tracker = cv.meanShift(dst, tracker, criteria)

      x,y,w,h = tracker
      img = cv.rectangle(frame, (x,y), (x+w,y+h), 255,2)
      cv.imshow('img',img)

      k = cv.waitKey(30) & 0xff
      if k==115:
         cv.imwrite('capture.png', img)
      if k == 27:
         break
    