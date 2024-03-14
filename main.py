import os

import numpy as np

from face_recgonize import *

path = "Faces"
images = []
names = []

faces = os.listdir(path)

for face in faces:
    image = cv2.imread(f"{path}/{face}")
    images.append(image)
    names.append(os.path.splitext(face)[0])

encodings = getEncodings(images)
print("Encoding completed")

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    cntFaces, cntEncodes = processFrame(img)
    for encoding, face in zip(cntEncodes,cntFaces):
        name = ""
        result, distance = compareImages(encodings, encoding)
        matchIndex = np.argmin(distance)

        if distance[matchIndex] < 5:
            name = names[matchIndex].upper()
            print(names[matchIndex])

        drawImage(img, face, name, name)




