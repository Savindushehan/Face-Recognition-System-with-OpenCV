import cv2 as cv
import numpy as np


blank = np.zeros((400,400),dtype='uint8' )

rectangle = cv.rectangle(blank.copy(),(30,30),(370,370),255 ,-1)
circle = cv.circle(blank.copy(), (200,200),200,255,-1)

cv.imshow('Rectangle', rectangle)
cv.imshow('Circle', circle)

# biutWise
bitwise_and = cv.bitwise_and(rectangle,circle)
cv.imshow('Bitwise AND ', bitwise_and)

#bitwise OR
bitwise_or = cv.bitwise_or(rectangle,circle)
cv.imshow('Bitwise OR',bitwise_or)

bitwise_xor = cv.bitwise_xor(rectangle,circle)
cv.imshow('Bitwise_XOR',bitwise_xor)

#bitwise NOT
bitwise_not = cv.bitwise_not(rectangle)
cv.imshow('Rectangle Not',bitwise_not)

cv.waitKey(0)