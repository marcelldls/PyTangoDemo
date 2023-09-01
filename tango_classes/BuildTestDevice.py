import time
from tango import DevState


def spin(self):
    time.sleep(1)


def dummy_measure_1_func(self):
    return 1.23


def dummy_measure_2_read(self):
    return self._measure_2


def dummy_measure_2_set(self, new):
    self._measure_2 = float(new)


attributes = {
    "dummy_measure_1": {
        "fget": dummy_measure_1_func,
        "dtype": float,
        },
    "dummy_measure_2": {
        "fget": dummy_measure_2_read,
        "fset": dummy_measure_2_set,
        "dtype": float,
        },
}

commands = {
    "spin": {
        "f": spin,
    },
}

properties = {
    "device_prop": {
        "dtype": str,
        },
}


def my_init(self):
    self.set_state(DevState.STANDBY)
    self._measure_2 = 2.23


dev_config = {
    "attributes": attributes,
    "commands": commands,
    "properties": properties,
    "init_method": my_init,
}
