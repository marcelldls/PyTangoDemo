from time import time, sleep
from tango import DevState, AttrQuality, AttrWriteType, DispLevel
from tango.server import Device, attribute, command, pipe
from tango.server import class_property, device_property
import re
import socket


class PytangoTempController(Device):

    def init_device(self):
        Device.init_device(self)
        self._suffix = ''.join(re.findall("[\d][\d]\Z", self.get_name()))
        self.set_state(DevState.ON)
        self.sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sckt.connect(( self.host, self.port))


    host = device_property(dtype=str)
    port = device_property(dtype=int)

    suffix = attribute(dtype=str)

    @suffix.read
    def suffix(self):
        return self._suffix

    """
    enabled = attribute(
                    dtype=bool, 
                    polling_period = 200,
                    )


    start = attribute(
                    dtype=int, 
                    polling_period = 200,
                    )

    current = attribute(
                    dtype=str, 
                    polling_period = 200,
                    )
    """

    end = attribute(
                dtype=int, 
                polling_period = 0,
                )
    
    @end.read
    def end(self):

        msg = f"E{self._suffix}?\r\n"
        self.sckt.send(msg.encode("utf-8"))
        msg_read = self.sckt.recv(1024)  # Keeping it simple
        self._end = int(msg_read.decode("utf-8"))

        return self._end
    
    @end.write
    def end(self, new_end):
        msg = f"E{self._suffix}={new_end}\r\n"
        self.sckt.send(msg.encode("utf-8"))


if __name__ == "__main__":
    PytangoTempController.run_server()
