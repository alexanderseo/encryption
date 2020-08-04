import os
import cv2 as cv
import numpy as np


class IdentifyFace:
    def __init__(self, photo):
        self.photo = photo

    def detect_face(self):
        with open(os.path.dirname(os.path.abspath(__file__)) + self.photo, 'rb') as in_memory_photo:
            face_cascade = cv.CascadeClassifier(cv.__path__[0] + "/data/haarcascade_frontalface_default.xml")
            in_memory_photo = in_memory_photo.read()
            nparr = np.frombuffer(in_memory_photo, np.uint8)
            img = cv.imdecode(nparr, 4)
            gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)
            if len(faces) > 0:
                return 'Лицо на фото обнаружено'
            else:
                return 'Лицо на фото не обнаружено'


if __name__ == "__main__":
    x = IdentifyFace('\panda.jpg')
    print(x.detect_face())