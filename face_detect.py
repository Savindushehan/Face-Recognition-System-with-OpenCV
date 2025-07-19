import cv2 as cv

img = cv.imread('Photos/group2.jpg')  # Make sure this file exists!
if img is None:
    print("Error: Image not found or path is incorrect")
    exit()

cv.imshow('Person', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Person', gray)

haar_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')

face_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=10)
print(f'Number of Faces found = {len(face_rect)}')

for (x, y, w, h) in face_rect:
    cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), thickness=2)

cv.imshow('Detected Faces', img)
cv.waitKey(0)
cv.destroyAllWindows()
