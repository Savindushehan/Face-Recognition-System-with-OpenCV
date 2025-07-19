import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('Photos/cat.jpg')
cv.imshow('Cats',img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('GRay',gray)

# Grayscale histogram
gray_hist = cv.calcHist([gray],[0],None,[256],[0,256])

plt.figure()
plt.title('Grayscale of Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixel')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()

cv.waitKey(0)