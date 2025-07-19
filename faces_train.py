import os
import cv2 as cv
import numpy as np

people = ['Oliver', 'Kusal', 'MaxWell']

DIR = r'D:\ALL Fun Project\Python Project With OpenCV\Photos\TrainPhotos'
haar_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')

features = []
labels = []

def create_train():
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path, img)

            img_array = cv.imread(img_path)
            if img_array is None:
                print(f"[Warning] Failed to read image: {img_path}")
                continue

            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

            for (x, y, w, h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)

create_train()

print(f'Length of the features = {len(features)}')
print(f'Length of the labels = {len(labels)}')
print("Training Done -----")

# Convert to numpy arrays
features = np.array(features, dtype='object')  # list of 2D arrays
labels = np.array(labels)

# Create LBPH face recognizer (make sure opencv-contrib-python is installed)
face_recognizer = cv.face.LBPHFaceRecognizer_create()

# Train the recognizer
face_recognizer.train(features, labels)

# Save model and data
face_recognizer.save('face_trained.yml')
np.save('features.npy', features)
np.save('labels.npy', labels)

print("Model and data saved successfully.")
