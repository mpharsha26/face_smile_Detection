#we use OpenCV library for this face recognition 
import cv2

#loading the cascades (series of filters to detect our face and eyes)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

#func to detect the face and the eyes given the input image
def detect(gray, frame):
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2) #creating a rectangle around the detected face
        roi_gray = gray[y:y+h, x:x+w] #roi --> region of interest  
        roi_color = frame[y:y+h, x:x+w] #to save some computational expenses, we detect the eyes only after we detect the face
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1,  15)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
    return frame
 
#applying our above function on each image coming from webcam
video_capture = cv2.VideoCapture(0)  #turning on the webcam
while True: #infinite loop to play the webcam and receive frames till user hits 's'
    _, frame = video_capture.read() 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
    canvas = detect(gray, frame)
    cv2.imshow('Video', canvas)
    if cv2.waitKey(1) & 0xFF == ord('s'):
        break
video_capture.release() #turning off the webcam
cv2.destroyAllWindows()