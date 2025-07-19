import cv2 as cv
import numpy as np

# Load image
img = cv.imread('Photos/cat.jpg')
cv.imshow('Cats', img)

# Convert to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

blank =np.zeros(img.shape[:2], dtype='init8')
cv.imshow('Blank',blank)

# Canny edge detection
canny = cv.Canny(img, 125, 175)
cv.imshow('Canny Edges', canny)

# Find contours
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)

print(f'🔍 Number of contours found: {len(contours)}')

# Create blank image to draw contours
blank = img.copy()
cv.drawContours(blank, contours, -1, (0, 255, 0), 2)
cv.imshow('Contours Drawn', blank)

cv.waitKey(0)
cv.destroyAllWindows()
