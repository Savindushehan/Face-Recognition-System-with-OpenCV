import cv2 as cv

img = cv.imread('Photos/stephan.jpg')
cv.imshow('Person',img)

gray= cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray Person',gray)

haar_cascade = cv.CascadeClassifier('haar_face.xml')

face_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1,minNeighbors=3)

print(f'Number of Faces found = {len(face_rect)}')

cv.waitKey(0)