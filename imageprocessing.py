import cv2
import numpy as np

IMAGE_SIZE = (224, 224)


def preprocess_image(image):
    """
    image: RGB numpy array (as produced by PIL -> np.array).
    Returns a (1, 224, 224, 3) float32 array scaled to [0, 1],
    matching the ImageDataGenerator(rescale=1./255) used in train.py.
    """
    image = cv2.resize(image, IMAGE_SIZE)
    image = image.astype("float32") / 255.0
    image = np.expand_dims(image, axis=0)
    return image
