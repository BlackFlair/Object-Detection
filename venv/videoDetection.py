import cv2
import numpy as np

video = cv2.VideoCapture(0)

a = 1

while True :
    a = a + 1
    check , frame = video.read()
    print(frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    face_cascade = cv2.CascadeClassifier("----------") # haar file path
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=5)
    cv2.imshow("----------", gray) #output screen name

    for x,y,w,h in faces :
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=5)
        gray = cv2.rectangle(gray,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.imshow("----------", gray) ##output screen name

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

print(a)

video.release()
cv2.destroyAllWindows()