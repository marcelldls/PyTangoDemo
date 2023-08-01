from tango.server import Device, attribute, command
from src.util import spin, dummy_measure_func


def device_class_builder(attributes=None,
                         commands=None,
                         properties=None):

    print("Building device class...")
    device_class = add_attributes(Device, attributes)
    device_class = add_commands(device_class, commands)
    device_class = add_properties(device_class, properties)

    return device_class


def add_attributes(device, attributes):

    class dynamic_class(device):
        dummy_measure = attribute(dummy_measure_func, dtype=float)

    print("Added attributes")

    return dynamic_class


def add_commands(device, commands):
    print("Added commands")
    return device


def add_properties(device, properties):
    print("Added properties")
    return device
