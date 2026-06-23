from glucose_guard import GlucoseGuard, GlucoseReading
import pytest
from datetime import datetime, timedelta

def test_update_glucose_reading():
    guard = GlucoseGuard()
    guard.update_glucose_reading(150)
    assert guard.get_live_glucose_value() == 150

def test_check_for_alert():
    guard = GlucoseGuard()
    guard.update_glucose_reading(200)
    assert guard.get_alert_status() == True

def test_dismiss_alert():
    guard = GlucoseGuard()
    guard.update_glucose_reading(200)
    guard.dismiss_alert()
    assert guard.get_alert_status() == False

def test_snooze_alert():
    guard = GlucoseGuard()
    guard.update_glucose_reading(200)
    guard.snooze_alert()
    assert guard.get_alert_status() == False

def test_get_live_glucose_value():
    guard = GlucoseGuard()
    guard.update_glucose_reading(150)
    assert guard.get_live_glucose_value() == 150

def test_get_alert_status():
    guard = GlucoseGuard()
    guard.update_glucose_reading(200)
    assert guard.get_alert_status() == True

def test_edge_case_no_readings():
    guard = GlucoseGuard()
    assert guard.get_live_glucose_value() is None
    assert guard.get_alert_status() == False
