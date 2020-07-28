import cv2

# Loading the cascades
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')

#function to detect our smile along with face and eyes 
def detect(gray, frame):
    faces = face_cascade.detectMultiScale(gray, 1.2, 7)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 22)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
        smiles = smile_cascade.detectMultiScale(roi_gray, 3, 15)
        for (sx, sy, sw, sh) in smiles:
            cv2.rectangle(roi_color, (sx, sy), (sx+sw, sy+sh), (0, 0, 255), 2)
    return frame

# #func to detect only smile
# def detect(gray, frame):
#     smiles = smile_cascade.detectMultiScale(gray, 3, 15)
#     for (x, y, w, h) in smiles:
#         cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
#     return frame

video_capture = cv2.VideoCapture(0)
while True:
    _, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    canvas = detect(gray, frame)
    cv2.imshow('Smile plzzzz MP !!', canvas)
    if cv2.waitKey(1) & 0xFF == ord('f'):
        break
video_capture.release()
cv2.destroyAllWindows()