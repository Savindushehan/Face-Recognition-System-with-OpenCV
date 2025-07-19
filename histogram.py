import cv2 as cv

img = cv.imread('Photos/cay.jpg')
cv.imshow('Cats',img)

gray = cv.cvtColor(img,cv.)