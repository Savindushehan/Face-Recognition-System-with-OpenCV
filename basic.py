import cv2 as cv

img = cv.imread('Photos/cat.jpg')
cv.imshow('Cat', img)

# 1. Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# 2. Blur
blur = cv.GaussianBlur(img, (3, 3), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# 3. Edge Cascade
canny = cv.Canny(img, 255, 175)
cv.imshow('Canny', canny)

# 4. Dilating the Image
dilated = cv.dilate(canny, (3, 3), iterations=1)
cv.imshow('Dilated', dilated)

# 5. Eroding
eroded = cv.erode(dilated, (3, 3), iterations=1)
cv.imshow("Eroded", eroded)

# 6. Resize
resized = cv.resize(img, (500, 500))
cv.imshow('Resized', resized)

# 7. Cropping
# Cropping uses array slicing, so correct syntax:
cropped = img[50:200, 200:400]  # [rows, columns]
cv.imshow('Cropped', cropped)

cv.waitKey(0)
cv.destroyAllWindows()
