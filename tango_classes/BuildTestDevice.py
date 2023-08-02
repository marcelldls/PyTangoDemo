import time


def spin():
    time.sleep(3)


def dummy_measure_func(self):
    return 1.23


attributes = {
    "dummy_measure_1": {
        "method": dummy_measure_func,
        "dtype": float,
        },
    "dummy_measure_2": {
        "method": dummy_measure_func,
        "dtype": float,
        },
}

commands = {
    "spin": spin,
}

properties = {
}

dev_config = {
    "attributes": attributes,
    "commands": commands,
    "properties": properties,
}
