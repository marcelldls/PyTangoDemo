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

dev_info = tango.DbDevInfo()
dev_info.server = dsr_name  # Device server instance name (Device factory)
dev_info._class = dsr_name[: dsr_name.find("/")]  # Device server: same name!
dev_info.name = dev_name  # Device instance name

db = tango.Database()
db.add_device(dev_info)

print("Registered Device:", dev_info.name, "- On device server:", dev_info.server)
