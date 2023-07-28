from time import sleep
from tango.server import Device, attribute, command

class PowerSupply(Device):

    """
    Instead of Device, could use Device_4Impl or Device_5Impl
    Device preferred as it will always use the latest version.
    """

    @attribute(dtype=float)
    def voltage(self):
        return 1.23

    @command
    def calibrate(self):
        sleep(0.1)

if __name__ == '__main__':
    PowerSupply.run_server()
