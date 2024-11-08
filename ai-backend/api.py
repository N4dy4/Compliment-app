# api.py
from fastapi import FastAPI, UploadFile, File
import cv2
import numpy as np
from capture import detect_landmarks, generate_compliment  # import your helper functions

app = FastAPI()

@app.post("/analyze")
async def analyze_image(file: UploadFile = File(...)):
    image_data = await file.read()
    nparr = np.fromstring(image_data, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    prominent_feature = detect_landmarks(img)  # Run feature detection
    compliment = generate_compliment(prominent_feature)  # Get a compliment
    return {"feature": prominent_feature, "compliment": compliment}
