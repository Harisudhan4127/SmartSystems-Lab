import tensorflow as tf
import cv2
import numpy as np

# Load the model
loaded_model = tf.saved_model.load('saved_model/my_model')

# Load Haarcascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Emotion labels
emotion_labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Neutral', 'Sad', 'Surprise']

# Start video capture
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    for (x, y, w, h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        roi_gray = cv2.resize(roi_gray, (48, 48))  # Resize to match model input
        roi_gray = roi_gray.astype('float32') / 255.0  # Normalize
        roi_gray = np.reshape(roi_gray, (1, 48, 48, 1))  # Reshape for model

        # Make predictions
        infer = loaded_model.signatures["serving_default"]
        predictions = infer(tf.convert_to_tensor(roi_gray))
        
        # Get the predicted class
        predicted_class = np.argmax(predictions['dense'].numpy(), axis=-1)
        predicted_emotion = emotion_labels[predicted_class[0]]

        # Draw rectangle around face and display emotion
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, predicted_emotion, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # Show the result
    cv2.imshow('Emotion Detection', frame)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
