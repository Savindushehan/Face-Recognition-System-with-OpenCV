import cv2 as cv
import numpy as np

# Create a blank color image (3 channels for BGR)
blank = np.zeros((500, 500, 3), dtype='uint8')  # shape: (500,500,3)

# Paint the whole image green (BGR: 0,255,0)
blank[200:300,300:400] = 0, 255, 0

#2. Draw a Rectangle
cv.rectangle(blank,(0,0),(250,250),(0,255,0), thickness=2)
cv.imshow('Rectangle', blank)

# 3.Draw A Circle
cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),40,(0,0,255),thickness=3)

#4. Draw a line
cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),40,(255,255,255),thickness=3)
cv.imshow('Line',blank)

# 5 write text
cv.putText(blank,'Hello', (255,255), cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,0),2)
cv.imshow('Text',blank)


cv.imshow('Green', blank)
cv.waitKey(0)
cv.destroyAllWindows()
