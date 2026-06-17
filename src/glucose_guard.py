import json
from dataclasses import dataclass
from typing import List
import random

@dataclass
class SensorData:
    glucose_level: float
    timestamp: int

class GlucoseGuardSimulator:
    def __init__(self, min_glucose: float, max_glucose: float, noise_level: float):
        self.min_glucose = min_glucose
        self.max_glucose = max_glucose
        self.noise_level = noise_level

    def generate_sensor_data(self, num_samples: int) -> List[SensorData]:
        sensor_data = []
        for i in range(num_samples):
            glucose_level = random.uniform(self.min_glucose, self.max_glucose)
            glucose_level += random.uniform(-self.noise_level, self.noise_level)
            sensor_data.append(SensorData(glucose_level, i))
        return sensor_data

    def customize_data_parameters(self, min_glucose: float, max_glucose: float, noise_level: float):
        self.min_glucose = min_glucose
        self.max_glucose = max_glucose
        self.noise_level = noise_level

    def integrate_with_analytics(self, sensor_data: List[SensorData]):
        # Simulate analytics integration by calculating average glucose level
        average_glucose = sum(data.glucose_level for data in sensor_data) / len(sensor_data)
        return average_glucose
