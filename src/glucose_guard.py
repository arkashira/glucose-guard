from dataclasses import dataclass
from enum import Enum

class MaterialType(Enum):
    SKIN_COMPATIBLE = 1
    NON_SKIN_COMPATIBLE = 2

@dataclass
class WearableDevice:
    material: MaterialType
    is_waterproof: bool
    is_ergonomic: bool

    def is_compatible(self):
        return self.material == MaterialType.SKIN_COMPATIBLE

    def is_comfortable(self):
        return self.is_ergonomic

    def is_durable(self):
        return self.is_waterproof

def create_wearable_device(material: MaterialType, is_waterproof: bool, is_ergonomic: bool) -> WearableDevice:
    return WearableDevice(material, is_waterproof, is_ergonomic)
