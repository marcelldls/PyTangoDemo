from tango import DevState
from tango.server import Device, attribute
from tango.server import device_property
import re
import socket


class PytangoTempController(Device):
    def init_device(self):
        Device.init_device(self)
        self._suffix = "".join(re.findall("[\d][\d]\Z", self.get_name()))
        self.set_state(DevState.ON)
        self.sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sckt.connect((self.host, self.port))

    # Properties

    host = device_property(dtype=str)
    port = device_property(dtype=int)

    # Attributes

    suffix = attribute(dtype=str)

    @suffix.read
    def suffix(self):
        return self._suffix

    enabled = attribute(
        dtype=bool,
        polling_period=0,
    )

    @enabled.read
    def enabled(self):
        self._enabled = bool(int(self.sckt_get("N")))
        return self._enabled

    @enabled.write
    def enabled(self, new_enabled):
        self.sckt_put("N", int(new_enabled))

    start = attribute(
        dtype=int,
        polling_period=0,
    )

    @start.read
    def enstartd(self):
        self._start = int(self.sckt_get("S"))
        return self._start

    @start.write
    def start(self, new_start):
        self.sckt_put("S", new_start)

    current = attribute(
        dtype=float,
        polling_period=0,
    )

    @current.read
    def current(self):
        self._current = float(self.sckt_get("T"))
        return self._current

    end = attribute(
        dtype=int,
        polling_period=0,
    )

    @end.read
    def end(self):
        self._end = int(self.sckt_get("E"))
        return self._end

    @end.write
    def end(self, new_end):
        self.sckt_put("E", new_end)

    # Helpers

    def sckt_put(self, prefix, msg):
        msg = f"{prefix}{self._suffix}={msg}\r\n"
        self.sckt.send(msg.encode("utf-8"))

    def sckt_get(self, prefix):
        msg = f"{prefix}{self._suffix}?\r\n"
        self.sckt.send(msg.encode("utf-8"))
        msg_read = self.sckt.recv(1024)  # Keeping it simple
        return msg_read.decode("utf-8")


if __name__ == "__main__":
    PytangoTempController.run_server()
