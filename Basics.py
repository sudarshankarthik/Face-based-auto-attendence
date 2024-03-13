import cv2
import numpy as np
import face_recognition


def loadImage(url):
    image = face_recognition.load_image_file(url)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    location = face_recognition.face_locations(image)[0]
    encoding = face_recognition.face_encodings(image)[0]

    return image, location, encoding


def drawImage(image, location, imageName="image", text=""):
    if location:
        cv2.rectangle(image, (location[3], location[0]), (location[1], location[2]), (0, 255, 0), 2)

    cv2.putText(image, text, (location[3], location[0] - 20), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,0))
    cv2.imshow(imageName, image)
    cv2.waitKey(0)


def compareImages(existing,test):
    result = face_recognition.compare_faces(existing,test)
    distance = face_recognition.face_distance(existing,test)

    return result,distance


imageChris, locChris, encodeChris = loadImage('./Base/chris-nolan.jpg')
imageTest, locTest, encodeTest = loadImage('./Base/christopher-nolan.jpg')
test2Image, test2Loc, test2Encode = loadImage('./Base/cllian-murphy.jpg')

testResult1, testDistance1 = compareImages([encodeChris],encodeTest)
testResult2, testDistance2 = compareImages([encodeChris],test2Encode)

drawImage(test2Image, test2Loc, "Cillian Image",f"${testResult2} ${testDistance2}")
drawImage(imageTest, locTest, "Test Image", f"${testResult1} ${testDistance1}")


