"""Register a device on a Tango database by command line"""

import argparse
import tango
from src.utils import config_parse
import re

parser = argparse.ArgumentParser(description="Register a Tango Device")
parser.add_argument(
    "deviceConfig",
    help="Specify a device configuration",
)
args = parser.parse_args()
cnfg = config_parse(args.deviceConfig)

dev_info = tango.DbDevInfo()
dev_info.server = cnfg.dsr_name  # Device server instance name (Device factory)
dev_info._class = re.findall("(.*)/", cnfg.dsr_name)[0]  # Device server: same name!
dev_info.name = cnfg.dev_name  # Device instance name

db = tango.Database()
db.delete_device(cnfg.dev_name)  # Remove existing device if any
db.add_device(dev_info)
db.put_device_property(dev_info.name, cnfg.dev_ptys)
db.put_class_property(dev_info._class, cnfg.cls_ptys)

read = db.get_device_info(dev_info.name)

print("Registered Device:", dev_info.name, "- On device server:", dev_info.server)
print(read)
print("Device properties", db.get_device_property_list(dev_info.name, '*'))
print("Class properties", db.get_class_property_list(dev_info._class))
