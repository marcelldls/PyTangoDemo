"""Register a device on a Tango database by command line"""

import argparse
import json
import tango

parser = argparse.ArgumentParser(description="Register a Tango Device")
parser.add_argument(
    "deviceConfig",
    help="Specify a device configuration",
)
args = parser.parse_args()

# Process config file
with open(args.deviceConfig, "r", encoding="utf-8") as config_file:
    config = json.load(config_file)
    cl_path = config["device_class_path"]
    dsr_name = config["device_server_name"]
    dev_name = config["device_name"]
    dev_ptys = config["device_properties"]
    cls_ptys = config["class_properties"]

dev_info = tango.DbDevInfo()
dev_info.server = dsr_name  # Device server instance name (Device factory)
dev_info._class = dsr_name[: dsr_name.find("/")]  # Device server: same name!
dev_info.name = dev_name  # Device instance name

db = tango.Database()
db.delete_device(dev_name)  # Remove existing device if any
db.add_device(dev_info)
db.put_device_property(dev_info.name, dev_ptys)
db.put_class_property(dev_info._class, cls_ptys)

read = db.get_device_info(dev_info.name)

print("Registered Device:", dev_info.name, "- On device server:", dev_info.server)
print(read)
print("Device properties", db.get_device_property_list(dev_info.name, '*'))
print("Class properties", db.get_class_property_list(dev_info._class))
