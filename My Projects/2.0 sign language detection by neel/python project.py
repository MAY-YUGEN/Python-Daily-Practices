import cv2
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array
import pyttsx3

# Load pre-trained model for hand gesture detection
model = load_model('path/to/pretrained_model.h5')

# Define classes for sign language gestures
classes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
           'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
           'U', 'V', 'W', 'X', 'Y', 'Z', 'del', 'nothing', 'space']

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Function to preprocess input frame
def preprocess_frame(frame):
    resized_frame = cv2.resize(frame, (224, 224))
    resized_frame = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2RGB)
    resized_frame = img_to_array(resized_frame)
    resized_frame = preprocess_input(resized_frame)
    return np.expand_dims(resized_frame, axis=0)

# Function to predict hand gesture and convert to text
def predict_gesture(frame):
    preprocessed_frame = preprocess_frame(frame)
    prediction = model.predict(preprocessed_frame)
    predicted_class = classes[np.argmax(prediction)]
    return predicted_class

# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Main function for real-time sign language detection
def sign_language_detection():
    cap = cv2.VideoCapture(0)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        # Flip the frame horizontally for a natural view
        frame = cv2.flip(frame, 1)

        # Draw a rectangle as the region of interest (ROI) for hand gesture
        cv2.rectangle(frame, (100, 100), (300, 300), (0, 255, 0), 2)
        
        # Extract the ROI
        roi = frame[100:300, 100:300]
        
        # Predict hand gesture and convert to text
        predicted_gesture = predict_gesture(roi)

        # Display the predicted gesture as text
        cv2.putText(frame, predicted_gesture, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        
        # Convert predicted gesture to spoken language
        speak(predicted_gesture)

        # Display the frame
        cv2.imshow('Real-Time Sign Language Detection', frame)

        # Exit loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the capture and close all windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    sign_language_detection()
