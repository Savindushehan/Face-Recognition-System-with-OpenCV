import cv2 as cv
import numpy as np

img = cv.imread('Photos/cat.jpg')
cv.imshow('Cat', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Laplacian
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))  # Fixed typo here
cv.imshow('Laplacian', lap)

#Sabel
sobelx = cv.Sobel(gray, cv.CV_64F,1, 0)
sobely = cv.Sobel(gray, cv.CV_64F,0, 1)
combined_sobel = cv.bitwise_or(sobelx,sobely)

cv.imshow('Sobel X',sobelx)
cv.imshow('Sobel Y',sobely)
cv.imshow('Sobel Y and X',combined_sobel)

canny = cv.Canny(gray,150,175)
cv.imshow('Canny',canny)

cv.waitKey(0)
