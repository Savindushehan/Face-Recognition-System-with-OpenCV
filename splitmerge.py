import cv2 as cv
import numpy as np

img = cv.imread('Photos/cat.jpg')
cv.imshow('Original', img)

# Split channels
b, g, r = cv.split(img)

# Create blank channel
blank = np.zeros(img.shape[:2], dtype='uint8')

# Merge to get color visualizations
blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

# Show each color channel as a color image
cv.imshow('Blue Channel', blue)
cv.imshow('Green Channel', green)
cv.imshow('Red Channel', red)

cv.waitKey(0)
cv.destroyAllWindows()
