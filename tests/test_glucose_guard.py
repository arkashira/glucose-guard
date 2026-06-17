from glucose_guard import GlucoseGuardSimulator, SensorData
import pytest

def test_generate_sensor_data():
    simulator = GlucoseGuardSimulator(50, 200, 10)
    sensor_data = simulator.generate_sensor_data(10)
    assert len(sensor_data) == 10
    for data in sensor_data:
        assert isinstance(data, SensorData)
        assert 50 - 10 <= data.glucose_level <= 200 + 10

def test_customize_data_parameters():
    simulator = GlucoseGuardSimulator(50, 200, 10)
    simulator.customize_data_parameters(60, 220, 15)
    assert simulator.min_glucose == 60
    assert simulator.max_glucose == 220
    assert simulator.noise_level == 15

def test_integrate_with_analytics():
    simulator = GlucoseGuardSimulator(50, 200, 10)
    sensor_data = [SensorData(100, 1), SensorData(120, 2), SensorData(110, 3)]
    average_glucose = simulator.integrate_with_analytics(sensor_data)
    assert average_glucose == (100 + 120 + 110) / 3

def test_generate_sensor_data_edge_case():
    simulator = GlucoseGuardSimulator(50, 200, 10)
    sensor_data = simulator.generate_sensor_data(0)
    assert len(sensor_data) == 0
