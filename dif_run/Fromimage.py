import cv2
import numpy as np
from keras.models import model_from_json

emotion_dict = {0: "angry", 1: "disgust", 2: "fear", 3: "happy", 4: "neutral", 5: "sad", 6: "surprise"}

from keras.models import load_model

# Load the model directly
emotion_model = load_model("Model.h5")
print("Loaded model from disk")

# Specify the path to the input image
# image_path = 'angry.jpg'
# image_path = 'disgust.jpg'
# image_path = 'fear.jpg'
# image_path = 'happy3.png'
# image_path = 'neutral.jpg'
image_path = 'sad3.png'
# image_path = 'suprise.png'

# Read the input image
frame = cv2.imread(image_path)
frame = cv2.resize(frame, (1280, 720))

# Convert the image to grayscale
gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
num_faces = face_detector.detectMultiScale(gray_frame, scaleFactor=1.3, minNeighbors=5)

# Process each detected face
for (x, y, w, h) in num_faces:
    cv2.rectangle(frame, (x, y-50), (x+w, y+h+10), (0, 255, 0), 4)
    roi_gray_frame = gray_frame[y:y + h, x:x + w]
    cropped_img = np.expand_dims(np.expand_dims(cv2.resize(roi_gray_frame, (48, 48)), -1), 0)

    # Predict the emotions
    emotion_prediction = emotion_model.predict(cropped_img)
    maxindex = int(np.argmax(emotion_prediction))
    cv2.putText(frame, emotion_dict[maxindex], (x+5, y-20), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)

# Display the result
cv2.imshow('Emotion Detection', frame)
cv2.waitKey(0)
cv2.destroyAllWindows()
