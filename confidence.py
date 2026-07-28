import numpy as np


def calculate_confidence(prediction):
    return float(np.max(prediction))
