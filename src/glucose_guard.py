import json
from dataclasses import dataclass
from datetime import datetime, timedelta
import time

@dataclass
class GlucoseReading:
    value: float
    timestamp: datetime

class GlucoseGuard:
    def __init__(self):
        self.readings = []
        self.alert_threshold = 180  # mg/dL
        self.alert_banner_visible = False

    def update_glucose_reading(self, value: float):
        self.readings.append(GlucoseReading(value, datetime.now()))
        self.check_for_alert()

    def check_for_alert(self):
        if self.readings and self.readings[-1].value > self.alert_threshold:
            self.alert_banner_visible = True
        else:
            self.alert_banner_visible = False

    def dismiss_alert(self):
        self.alert_banner_visible = False

    def snooze_alert(self):
        self.alert_banner_visible = False
        # snooze logic can be added here, e.g., set a timer to re-enable the alert

    def get_live_glucose_value(self):
        if self.readings:
            return self.readings[-1].value
        else:
            return None

    def get_alert_status(self):
        return self.alert_banner_visible
