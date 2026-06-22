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

    def predict_trend(self) -> float:
        # Simple moving average model
        if len(self.readings) < 2:
            return 0.0
        return (self.readings[-1].value - self.readings[-2].value) / (self.readings[-1].timestamp - self.readings[-2].timestamp)

    def get_confidence_score(self, prediction: float) -> float:
        # Simple confidence score based on the number of readings
        return min(1.0, len(self.readings) / 10.0)

    def get_5_minute_trend_prediction(self) -> (float, float):
        prediction = self.predict_trend()
        confidence_score = self.get_confidence_score(prediction)
        return prediction, confidence_score
