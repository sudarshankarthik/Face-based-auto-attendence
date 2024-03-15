import cv2
import face_recognition


def getEncodings(images):
    encodings = []

    for image in images:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        encoding = face_recognition.face_encodings(image)[0]

        encodings.append(encoding)

    return encodings

def processFrame(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    faces = face_recognition.face_locations(image)

    encodings = face_recognition.face_encodings(image,faces)

    return  faces, encodings


def drawImage(image, location, imageName="image", text=""):
    if location:
        cv2.rectangle(image, (location[3], location[0]), (location[1], location[2]), (0, 255, 0), 2)
        cv2.putText(image, text, (location[3], location[0] - 20), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,0))
    cv2.imshow(imageName, image)
    cv2.waitKey(1)


def compareImages(existing,test):
    result = face_recognition.compare_faces(existing,test)
    distance = face_recognition.face_distance(existing,test)

    return result,distance