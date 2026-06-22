from glucose_guard import GlucoseGuard, GlucoseReading
import pytest

def test_predict_trend():
    readings = [
        GlucoseReading(100.0, 0),
        GlucoseReading(120.0, 5),
        GlucoseReading(140.0, 10)
    ]
    guard = GlucoseGuard(readings)
    prediction = guard.predict_trend()
    assert prediction == 4.0

def test_get_confidence_score():
    readings = [
        GlucoseReading(100.0, 0),
        GlucoseReading(120.0, 5),
        GlucoseReading(140.0, 10)
    ]
    guard = GlucoseGuard(readings)
    prediction = guard.predict_trend()
    confidence_score = guard.get_confidence_score(prediction)
    assert confidence_score == 0.3

def test_get_5_minute_trend_prediction():
    readings = [
        GlucoseReading(100.0, 0),
        GlucoseReading(120.0, 5),
        GlucoseReading(140.0, 10)
    ]
    guard = GlucoseGuard(readings)
    prediction, confidence_score = guard.get_5_minute_trend_prediction()
    assert prediction == 4.0
    assert confidence_score == 0.3

def test_edge_case_empty_readings():
    guard = GlucoseGuard([])
    prediction = guard.predict_trend()
    assert prediction == 0.0

def test_edge_case_single_reading():
    readings = [
        GlucoseReading(100.0, 0)
    ]
    guard = GlucoseGuard(readings)
    prediction = guard.predict_trend()
    assert prediction == 0.0
