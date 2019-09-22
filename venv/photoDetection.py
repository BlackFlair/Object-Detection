import cv2
import numpy as np

fCascade = cv2.CascadeClassifier("----------") # haar file path

img = cv2.imread("----------",1) # test image path

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = fCascade.detectMultiScale(gray,scaleFactor=1.05,minNeighbors=5)

for x,y,w,h in faces :
    img = cv2.rectangle(img, (x,y), (x+h,y+h), (0,255,0), 2)

resized = cv2.resize(img, (600,600))

cv2.imshow("----------",resized) #output screen name
cv2.waitKey(0)
cv2.destroyAllWindows()