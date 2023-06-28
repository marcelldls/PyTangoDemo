"""Register a device on a Tango database"""

from __future__ import print_function
from builtins import open
import json
import tango

with open("config.json", "r", encoding="utf-8") as config_file:
    config = json.load(config_file)
    cl_path = config["device_class_path"]
    dsr_name = config["device_server_name"]
    dev_name = config["device_name"]

dev_info = tango.DbDevInfo()
dev_info.server = dsr_name  # Device server instance name (Device factory)
dev_info._class = dsr_name[:dsr_name.find('/')]  # Device server must same name
dev_info.name = dev_name  # Device instance name

db = tango.Database()
db.add_device(dev_info)

print("Registered:", dev_info.name)
