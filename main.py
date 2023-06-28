"""Exploring PyTango"""
from __future__ import print_function
import tango
print(tango.__version__)
print(tango.ApiUtil.get_env_var("TANGO_HOST"))

test_device = tango.DeviceProxy("test/test_device/0")
print("Ping device:", test_device.ping(), "us")
