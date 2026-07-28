import os
import numpy as np
from tensorflow.keras.models import load_model

from preprocessing.imageprocessing import preprocess_image
from utils.labels import CLASS_NAMES
from utils.confidence import calculate_confidence

# Project paths
# This file lives at <BASE_DIR>/model/predict.py, so going up two levels
# from this file gets back to the project root.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "model", "freshness_model.keras")

# Load model once, at import time
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(
        f"Model file not found at {MODEL_PATH}.\n"
        "Train a model first with train.py, or place your "
        "'freshness_model.keras' file inside the 'model' folder."
    )

model = load_model(MODEL_PATH)


def predict_freshness(image):
    """
    image: RGB numpy array.
    Returns (label: str, confidence: float, raw_prediction: np.ndarray)
    """
    processed_image = preprocess_image(image)
    prediction = model.predict(processed_image, verbose=0)
    predicted_index = int(np.argmax(prediction))
    label = CLASS_NAMES[predicted_index]
    confidence = calculate_confidence(prediction)
    return label, confidence, prediction
