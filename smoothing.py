import cv2 as cv

img = cv.imread('Photos/cat.jpg')
cv.imshow('Cat', img)


#Averagin
average = cv.blur(img, (3,3))
cv.imshow('Average Blur',average)

# Gaussion Blur
gauss = cv.GaussianBlur(img,(7,7),0)
cv.imshow('Gaussing Blur',gauss)

# Median blur
median = cv.medianBlur(img,7)
cv.imshow('Median',median)


cv.waitKey(0)
