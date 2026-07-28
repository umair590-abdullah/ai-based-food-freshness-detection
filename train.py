import os
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Input, Conv2D, MaxPooling2D, Flatten, Dense, Dropout

# -----------------------------
# Configuration
# -----------------------------
IMAGE_SIZE = (224, 224)
BATCH_SIZE = 32
EPOCHS = 10

# Project paths
# train.py lives directly at the project root, so BASE_DIR is just this
# file's own directory (NOT dirname(dirname(...)) - that would walk one
# level too far up, outside the project).
# Project paths
# train.py lives inside the 'model' directory. 
# We use dirname twice to go up one level to the true project root directory.
MODEL_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(MODEL_DIR)

DATASET_PATH = os.path.join(BASE_DIR, "data")
MODEL_PATH = os.path.join(MODEL_DIR, "freshness_model.keras")


# -----------------------------
# Data Generator
# -----------------------------
train_datagen = ImageDataGenerator(
    rescale=1.0 / 255,
    validation_split=0.2
)

train_data = train_datagen.flow_from_directory(
    DATASET_PATH,
    target_size=IMAGE_SIZE,
    batch_size=BATCH_SIZE,
    class_mode="categorical",
    subset="training",
    shuffle=True
)

validation_data = train_datagen.flow_from_directory(
    DATASET_PATH,
    target_size=IMAGE_SIZE,
    batch_size=BATCH_SIZE,
    class_mode="categorical",
    subset="validation",
    shuffle=False
)

# -----------------------------
# CNN Model
# -----------------------------
model = Sequential([
    Input(shape=(224, 224, 3)),

    Conv2D(32, (3, 3), activation="relu"),
    MaxPooling2D((2, 2)),

    Conv2D(64, (3, 3), activation="relu"),
    MaxPooling2D((2, 2)),

    Conv2D(128, (3, 3), activation="relu"),
    MaxPooling2D((2, 2)),

    Flatten(),

    Dense(128, activation="relu"),
    Dropout(0.5),

    Dense(3, activation="softmax")
])

# -----------------------------
# Compile Model
# -----------------------------
model.compile(
    optimizer="adam",
    loss="categorical_crossentropy",
    metrics=["accuracy"]
)

# -----------------------------
# Train Model
# -----------------------------
history = model.fit(
    train_data,
    validation_data=validation_data,
    epochs=EPOCHS
)

# -----------------------------
# Save Model
# -----------------------------
os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)
model.save(MODEL_PATH)

print("\nModel training completed successfully!")
print(f"Model saved at:\n{MODEL_PATH}")
