import cv2
import mediapipe as mp

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=True, max_num_faces=1)

# Load an image
img = cv2.imread('face.jpg')
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

results = face_mesh.process(img_rgb)
if results.multi_face_landmarks:
    for face_landmarks in results.multi_face_landmarks:
        # Loop through landmarks to access feature points
        for id, landmark in enumerate(face_landmarks.landmark):
            # Calculate pixel coordinates
            x, y = int(landmark.x * img.shape[1]), int(landmark.y * img.shape[0])
            cv2.circle(img, (x, y), 1, (0, 255, 0), -1)
