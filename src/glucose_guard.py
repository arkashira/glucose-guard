import json
from dataclasses import dataclass
from typing import List

@dataclass
class GlucoseReading:
    value: float
    timestamp: int

class GlucoseGuard:
    def __init__(self, readings: List[GlucoseReading]):
        self.readings = readings
        self.model = None  # Initialize model as None

    def train_model(self):
        # Simple moving average model for demonstration purposes
        self.model = [reading.value for reading in self.readings]

    def predict_trend(self):
        if self.model is None:  # Check if model is None
            raise ValueError("Model not trained")
        # Simple prediction based on last 5 readings
        last_readings = self.model[-5:] if len(self.model) >= 5 else self.model
        trend = sum(last_readings) / len(last_readings)
        confidence = 0.8  # Fixed confidence for demonstration
        return trend, confidence

    def get_prediction(self):
        trend, confidence = self.predict_trend()
        return {"trend": trend, "confidence": confidence}
