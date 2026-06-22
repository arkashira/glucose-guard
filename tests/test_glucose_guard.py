from glucose_guard import GlucoseGuard, GlucoseReading
import pytest

def test_train_model():
    readings = [GlucoseReading(100, 1), GlucoseReading(120, 2), GlucoseReading(110, 3)]
    guard = GlucoseGuard(readings)
    guard.train_model()
    assert guard.model == [100, 120, 110]

def test_predict_trend():
    readings = [GlucoseReading(100, 1), GlucoseReading(120, 2), GlucoseReading(110, 3)]
    guard = GlucoseGuard(readings)
    guard.train_model()
    trend, confidence = guard.predict_trend()
    assert trend == 110
    assert confidence == 0.8

def test_get_prediction():
    readings = [GlucoseReading(100, 1), GlucoseReading(120, 2), GlucoseReading(110, 3)]
    guard = GlucoseGuard(readings)
    guard.train_model()
    prediction = guard.get_prediction()
    assert prediction["trend"] == 110
    assert prediction["confidence"] == 0.8

def test_model_not_trained():
    guard = GlucoseGuard([])
    with pytest.raises(ValueError):
        guard.predict_trend()
