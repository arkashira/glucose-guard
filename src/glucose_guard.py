import json
from dataclasses import dataclass
from datetime import datetime, timedelta
import statistics

@dataclass
class GlucoseReading:
    value: float
    timestamp: datetime

class GlucoseGuard:
    def __init__(self, readings):
        self.readings = readings

    def predict_trend(self):
        values = [reading.value for reading in self.readings]
        if len(values) < 2:
            return None
        trend = statistics.linear_regression(values, [i for i in range(len(values))])
        return trend

    def check_hypo_hyper(self, trend):
        if trend is None:
            return None
        predicted_value = trend[0] * (len(self.readings) + 1) + trend[1]
        if predicted_value < 70:
            return "hypo"
        elif predicted_value > 180:
            return "hyper"
        else:
            return None

    def send_alert(self, event):
        if event:
            print(f"Sending alert: {event}")
            return True
        return False

    def log_alert(self, event):
        if event:
            print(f"Logging alert: {event}")
            return True
        return False

    def acknowledge_alert(self, event):
        if event:
            print(f"Acknowledging alert: {event}")
            return True
        return False

    def dismiss_alert(self, event):
        if event:
            print(f"Dismissing alert: {event}")
            return True
        return False
