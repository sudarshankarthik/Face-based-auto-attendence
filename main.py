import os

import numpy as np

from face_recgonize import *
from Attendence import *

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
    if not success:
        continue
    cntFaces, cntEncodes = processFrame(img)
    for encoding, face in zip(cntEncodes,cntFaces):
        name = ""
        result, distance = compareImages(encodings, encoding)
        matchIndex = np.argmin(distance)

        if distance[matchIndex] < 0.5:
            name = names[matchIndex].upper()
            markAttendence(names[matchIndex])

        drawImage(img, face, "Live feed", name)





