import cv2 as cv
import numpy as np

# Load image
img = cv.imread('Photos/cat.jpg')
cv.imshow('Cat', img)

# -------------------- Translate Function --------------------
def translate(img, x, y):
    # Create translation matrix
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])  # (width, height)
    return cv.warpAffine(img, transMat, dimensions)

# Translate image (-100 pixels in x, +100 pixels in y)
translated = translate(img, -100, 100)
cv.imshow('Translated', translated)

# -------------------- Rotate Function --------------------
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width // 2, height // 2)

    # Create rotation matrix
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)

# Rotate image (-45 degrees counterclockwise)
rotated = rotate(img, -45)
cv.imshow('Rotated', rotated)


#Flipping

flip = cv.flip(img,0)
cv.imshow('Flip',flip)



cv.waitKey(0)
cv.destroyAllWindows()
