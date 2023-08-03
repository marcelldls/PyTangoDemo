from time import time, sleep
from tango import DevState, AttrQuality, AttrWriteType, DispLevel
from tango.server import Device, attribute, command, pipe
from tango.server import class_property, device_property


class PytangoTestDevice(Device):

    """
    Instead of Device, could use Device_4Impl or Device_5Impl
    Device preferred as it will always use the latest version.
    """

    # Properties

    host = device_property(dtype=str)
    port = class_property(dtype=int, default_value=9788)

    # Atttributes in two ways

    @attribute(dtype=float)
    def voltage(self):
        return 1.23

    current = attribute(
        label="Current", dtype=float,
        display_level=DispLevel.EXPERT,
        access=AttrWriteType.READ_WRITE,
        unit="A", format="8.4f",
        min_value=0.0, max_value=8.5,
        min_alarm=0.1, max_alarm=8.4,
        min_warning=0.5, max_warning=8.0,
        fget="get_current", fset="set_current",
        doc="the power supply current"
        )

    def get_current(self):
        return 2.3456, time(), AttrQuality.ATTR_WARNING

    def set_current(self, current):
        print("Current set to %f" % current)

    # Commands

    @command
    def calibrate(self):
        sleep(0.1)

    # Pipes

    @pipe
    def info(self):
        return ('Information',
                dict(manufacturer='Tango',
                     model='PS2000',
                     version_number=123,
                     ))

if __name__ == "__main__":
    PytangoTestDevice.run_server()
