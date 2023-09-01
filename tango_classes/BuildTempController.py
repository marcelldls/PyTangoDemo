from tango import DevState
import re
import socket


def suffix_read(self):
    return self._suffix


def enabled_read(self):
    self._enabled = bool(int(self.sckt_get("N")))
    return self._enabled


def enabled_write(self, new_enabled):
    self.sckt_put("N", int(new_enabled))


def start_read(self):
    self._start = int(self.sckt_get("S"))
    return self._start


def start_write(self, new_start):
    self.sckt_put("S", new_start)


def current_read(self):
    self._current = float(self.sckt_get("T"))
    return self._current


def end_read(self):
    self._end = int(self.sckt_get("E"))
    return self._end


def end_write(self, new_end):
    self.sckt_put("E", new_end)


attributes = {
    "suffix": {
        "dtype": str,
        "fget": suffix_read,
        },
    "enabled": {
        "dtype": bool,
        "polling_period": 0,
        "fget": enabled_read,
        "fset": enabled_write,
        },
    "start": {
        "dtype": int,
        "polling_period": 0,
        "fget": start_read,
        "fset": start_write,
        },
    "current": {
        "dtype": float,
        "polling_period": 0,
        "fget": current_read,
        },
    "end": {
        "dtype": int,
        "polling_period": 0,
        "fget": end_read,
        "fset": end_write,
        },
}

properties = {
    "host": {
        "dtype": str,
        },
    "port": {
        "dtype": int,
        },
}


def my_init(self):
    self._suffix = "".join(re.findall("[\d][\d]\Z", self.get_name()))
    self.set_state(DevState.ON)
    self.sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.sckt.connect((self.host, self.port))


def sckt_put(self, prefix, msg):
    msg = f"{prefix}{self._suffix}={msg}\r\n"
    self.sckt.send(msg.encode("utf-8"))


def sckt_get(self, prefix):
    msg = f"{prefix}{self._suffix}?\r\n"
    self.sckt.send(msg.encode("utf-8"))
    msg_read = self.sckt.recv(1024)
    return msg_read.decode("utf-8")


helpers = {
    "sckt_put": sckt_put,
    "sckt_get": sckt_get,
}

dev_config = {
    "attributes": attributes,
    "properties": properties,
    "init_method": my_init,
    "helpers": helpers
}
