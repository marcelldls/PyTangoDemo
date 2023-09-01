from time import sleep
from tango import DevState, AttrWriteType, DispLevel
from tango.server import Device, attribute, command, pipe
from tango.server import class_property, device_property


class PytangoTestDevicePlus(Device):

    """
    Instead of Device, could use Device_4Impl or Device_5Impl
    Device preferred as it will always use the latest version.
    """

    def init_device(self):
        Device.init_device(self)
        self.__current = 0.0
        self.set_state(DevState.STANDBY)

    # Properties

    device_prop = device_property(dtype=str)
    class_prop = class_property(dtype=int, default_value=42)

    # Atttributes in two ways

    @attribute(dtype=float)
    def voltage(self):
        return 1.23

    current = attribute(
        label="Current",
        dtype=float,
        display_level=DispLevel.EXPERT,
        access=AttrWriteType.READ_WRITE,
        unit="A",
        format="8.4f",
        min_value=0.0,
        max_value=8.5,
        min_alarm=0.1,
        max_alarm=8.4,
        min_warning=0.5,
        max_warning=8.0,
        fget="get_current",
        fset="set_current",
        doc="the power supply current",
        polling_period=1000  # ms (Client calls don't trigger get)
    )

    def get_current(self):
        self.__current = self.__current + 1
        return self.__current

    def set_current(self, current):
        # should set the power supply current
        self.__current = current

    # Commands in two ways

    @command
    def calibrate_1(self):
        sleep(0.1)

    def calibrate_2(self):
        sleep(0.1)

    calibrate_2 = command(calibrate_2)

    # Pipes

    @pipe
    def info(self):
        return ('Information',
                dict(manufacturer='Tango',
                     model='PS2000',
                     version_number=123,
                     ))


if __name__ == "__main__":
    PytangoTestDevicePlus.run_server()
