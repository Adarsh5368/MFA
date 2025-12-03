
# import face_recognition
# import numpy as np
# import pickle

# def encode_face(image_path):
#     image = face_recognition.load_image_file(image_path)
#     encoding = face_recognition.face_encodings(image)
#     return encoding[0] if encoding else None

# def compare_faces(known_encoding, new_image_path):
#     new_encoding = encode_face(new_image_path)
#     if new_encoding is None:
#         return False
#     return face_recognition.compare_faces([known_encoding], new_encoding)[0]
import cv2
import numpy as np
import tempfile
import os

def train_face_model(image_bytes):
    # Convert bytes to grayscale image
    np_arr = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(np_arr, cv2.IMREAD_GRAYSCALE)

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    faces = face_cascade.detectMultiScale(img, 1.1, 4)

    if len(faces) == 0:
        return None, "No face detected"

    x, y, w, h = faces[0]
    face_img = img[y:y+h, x:x+w]

    # Train LBPH model
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.train([face_img], np.array([0]))

    # Save to temp file, read back as bytes
    with tempfile.NamedTemporaryFile(delete=False) as tmpfile:
        recognizer.write(tmpfile.name)
        tmpfile.seek(0)
        model_bytes = open(tmpfile.name, "rb").read()
    os.unlink(tmpfile.name)

    return model_bytes, None


def verify_face_model(model_bytes, image_bytes):
    np_arr = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(np_arr, cv2.IMREAD_GRAYSCALE)

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    faces = face_cascade.detectMultiScale(img, 1.1, 4)

    if len(faces) == 0:
        return None, None, "No face detected"

    x, y, w, h = faces[0]
    face_img = img[y:y+h, x:x+w]

    with tempfile.NamedTemporaryFile(delete=False) as tmpfile:
        tmpfile.write(model_bytes)
        tmpfile.close()

        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.read(tmpfile.name)
    os.unlink(tmpfile.name)

    label, confidence = recognizer.predict(face_img)
    return label, confidence, None
