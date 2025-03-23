import cv2
import os

# Define the path to the Haarcascade file (ensure it's in the working directory or specify full path)
HAAR_FILE = r"C:\Users\lalit\OneDrive\Desktop\face detection\HAAR_FILE.xml"

# Validate Haarcascade file existence
if not os.path.exists(HAAR_FILE):
    raise FileNotFoundError(f"Haarcascade file '{HAAR_FILE}' not found. Ensure it's in the correct directory.")

# Load Haarcascade classifier
face_cascade = cv2.CascadeClassifier(HAAR_FILE)

# Open webcam (0 for default camera, change if using an external camera)
camera = cv2.VideoCapture(0)

if not camera.isOpened():
    raise RuntimeError("Error: Could not open webcam. Check if the camera is connected and accessible.")

while True:
    # Capture frame from webcam
    ret, frame = camera.read()
    if not ret:
        print("Error: Failed to capture image from webcam.")
        break
    
    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    # Draw rectangles around detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
    
    # Display the frame with detected faces
    cv2.imshow('Live Face Detection', frame)
    
    # Break loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all windows
camera.release()
cv2.destroyAllWindows()
