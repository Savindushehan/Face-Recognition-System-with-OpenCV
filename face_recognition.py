import numpy as np
import cv2 as cv

# Load Haar Cascade and face recognizer
haar_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')
face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')  # Fix: filename typo

# Load label names and data
people = ['Oliver', 'Kusal', 'MaxWell']
features = np.load('features.npy', allow_pickle=True)
labels = np.load('labels.npy')

# Load and process image for recognition
img = cv.imread(r'D:\ALL Fun Project\Python Project With OpenCV\Photos\TrainPhotos\Kusal\K2.jpeg')  # Add extension
if img is None:
    print("Error: Image not found")
    exit()

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Person', gray)

# Detect faces
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

for (x, y, w, h) in faces_rect:
    faces_roi = gray[y:y+h, x:x+w]  # Fix: use x+w not x+h

    label, confidence = face_recognizer.predict(faces_roi)  # Fix: .predict(), not .predoct()
    print(f'Label = {people[label]} with a confidence of {confidence:.2f}')

    cv.putText(img, str(people[label]), (x, y - 10), cv.FONT_HERSHEY_COMPLEX, 1.0, (0, 255, 0), thickness=2)
    cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), thickness=2)

cv.imshow('Detected Face', img)
cv.waitKey(0)
cv.destroyAllWindows()
