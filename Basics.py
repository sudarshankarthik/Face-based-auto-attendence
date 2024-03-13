import cv2
import numpy as np
import face_recognition

imageChris = face_recognition.load_image_file('./Base/chris-nolan.jpg')
imageChris = cv2.cvtColor(imageChris, cv2.COLOR_BGR2RGB)

imageTest = face_recognition.load_image_file('./Base/christopher-nolan.jpg')
imageTest = cv2.cvtColor(imageTest, cv2.COLOR_BGR2RGB)

faceLocChris = face_recognition.face_locations(imageChris)[0]
encodeChris = face_recognition.face_encodings(imageChris)[0]

cv2.rectangle(imageChris, (faceLocChris[3], faceLocChris[0]), (faceLocChris[1], faceLocChris[2]), (0, 255, 0), 2)
cv2.imshow('ChrisNolan', imageChris)
cv2.waitKey(0)

faceLocTest = face_recognition.face_locations(imageTest)[0]
encodeTest = face_recognition.face_encodings(imageTest)[0]

cv2.rectangle(imageTest, (faceLocTest[3], faceLocTest[0]), (faceLocTest[1], faceLocTest[2]), (0, 255, 0), 2)
cv2.imshow('ChrisNolan', imageTest)
cv2.waitKey(0)
