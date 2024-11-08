import streamlit as st
import cv2
import mediapipe as mp
import numpy as np
from PIL import Image

# Initialize MediaPipe FaceMesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=True, max_num_faces=1)

# Function to detect landmarks and return an image with marked points
def detect_landmarks(image):
    # Convert the PIL image to a format suitable for OpenCV
    img_array = np.array(image)
    img_rgb = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)
    
    # Process the image to detect facial landmarks
    results = face_mesh.process(img_rgb)
    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            for id, landmark in enumerate(face_landmarks.landmark):
                x, y = int(landmark.x * img_rgb.shape[1]), int(landmark.y * img_rgb.shape[0])
                cv2.circle(img_rgb, (x, y), 1, (0, 255, 0), -1)
    # Convert the processed image back to RGB format for Streamlit
    return cv2.cvtColor(img_rgb, cv2.COLOR_BGR2RGB)

# Streamlit UI
st.title("AI Compliment Generator")

uploaded_image = st.file_uploader("Upload an image", type=["jpg", "png"])
if uploaded_image is not None:
    # Open and display the uploaded image
    image = Image.open(uploaded_image)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    
    # Detect landmarks and generate a compliment
    processed_image = detect_landmarks(image)
    st.image(processed_image, caption="Image with Landmarks", use_column_width=True)

    # Generate and display a compliment (adjust the function to detect specific features as needed)
    st.write("Your eyes are captivating!")  # This can be replaced with a function for dynamic compliments
