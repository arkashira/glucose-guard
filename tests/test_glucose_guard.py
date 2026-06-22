from glucose_guard import create_wearable_device, WearableDevice, MaterialType

def test_wearable_device_compatibility():
    device = create_wearable_device(MaterialType.SKIN_COMPATIBLE, True, True)
    assert device.is_compatible() == True
    assert device.is_comfortable() == True
    assert device.is_durable() == True

def test_wearable_device_incompatibility():
    device = create_wearable_device(MaterialType.NON_SKIN_COMPATIBLE, True, True)
    assert device.is_compatible() == False
    assert device.is_comfortable() == True
    assert device.is_durable() == True

def test_wearable_device_non_ergonomic():
    device = create_wearable_device(MaterialType.SKIN_COMPATIBLE, True, False)
    assert device.is_compatible() == True
    assert device.is_comfortable() == False
    assert device.is_durable() == True

def test_wearable_device_non_waterproof():
    device = create_wearable_device(MaterialType.SKIN_COMPATIBLE, False, True)
    assert device.is_compatible() == True
    assert device.is_comfortable() == True
    assert device.is_durable() == False
