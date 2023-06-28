"""Exploring PyTango"""
from __future__ import print_function
import json
import tango

with open("config.json", "r", encoding="utf-8") as config_file:
    config = json.load(config_file)
    cl_path = config["device_class_path"]
    dsr_name = config["device_server_name"]
    dev_name = config["device_name"]

print(tango.__version__)
print(tango.ApiUtil.get_env_var("TANGO_HOST"))

test_device = tango.DeviceProxy(dev_name)
print("Ping device:", test_device.ping(), "us")
