import cv2
import numpy as np
import face_recognition


def loadImage(url):
    image = face_recognition.load_image_file(url)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    location = face_recognition.face_locations(image)[0]
    encoding = face_recognition.face_encodings(image)[0]

    return image, location, encoding


def drawImage(image, location, imageName="image"):
    if location:
        cv2.rectangle(image, (location[3], location[0]), (location[1], location[2]), (0, 255, 0), 2)
    cv2.imshow(imageName, image)
    cv2.waitKey(0)


imageChris, locChris, encodeChris = loadImage('./Base/chris-nolan.jpg')
imageTest, locTest, encodeTest = loadImage('./Base/christopher-nolan.jpg')

result = face_recognition.compare_faces([encodeChris], encodeTest)
print(result)

drawImage(imageChris, locChris, "Chris Image")
drawImage(imageTest, locTest, "Test Image")


