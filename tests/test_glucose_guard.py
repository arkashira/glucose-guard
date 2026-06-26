from glucose_guard import GlucoseGuard, GlucoseReading
from datetime import datetime, timedelta
import pytest

@pytest.fixture
def readings():
    return [
        GlucoseReading(100, datetime.now() - timedelta(minutes=10)),
        GlucoseReading(120, datetime.now() - timedelta(minutes=5)),
        GlucoseReading(140, datetime.now())
    ]

def test_predict_trend(readings):
    guard = GlucoseGuard(readings)
    trend = guard.predict_trend()
    assert trend is not None

def test_check_hypo_hyper(readings):
    guard = GlucoseGuard(readings)
    trend = guard.predict_trend()
    event = guard.check_hypo_hyper(trend)
    assert event is not None

def test_send_alert(readings):
    guard = GlucoseGuard(readings)
    trend = guard.predict_trend()
    event = guard.check_hypo_hyper(trend)
    assert guard.send_alert(event)

def test_log_alert(readings):
    guard = GlucoseGuard(readings)
    trend = guard.predict_trend()
    event = guard.check_hypo_hyper(trend)
    assert guard.log_alert(event)

def test_acknowledge_alert(readings):
    guard = GlucoseGuard(readings)
    trend = guard.predict_trend()
    event = guard.check_hypo_hyper(trend)
    assert guard.acknowledge_alert(event)

def test_dismiss_alert(readings):
    guard = GlucoseGuard(readings)
    trend = guard.predict_trend()
    event = guard.check_hypo_hyper(trend)
    assert guard.dismiss_alert(event)

def test_edge_case_no_readings():
    guard = GlucoseGuard([])
    trend = guard.predict_trend()
    assert trend is None

def test_edge_case_single_reading():
    guard = GlucoseGuard([GlucoseReading(100, datetime.now())])
    trend = guard.predict_trend()
    assert trend is None
