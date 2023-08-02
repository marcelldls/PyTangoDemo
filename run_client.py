"""Command line Tango Device Client"""
from __future__ import print_function
from builtins import open
import argparse
import json
import tango

# Process command line arguments
parser = argparse.ArgumentParser(description="Run a Tango Client")
parser.add_argument(
    "--nodb",
    help="Connect to a device server without a database",
    action="store_true"
)
parser.add_argument(
    "--test",
    help="Connect to a test device server (no database)",
    action="store_true"
)
parser.add_argument(
    "--add",
    help="Additional complexity that needs implementation to work",
    action="store_true"
)
args = parser.parse_args()

# Process config file
with open("config/config.json", "r", encoding="utf-8") as config_file:
    config = json.load(config_file)
    host = config["host"]
    port = config["port"]
    dsr_name = config["device_server_name"]
    dev_name = config["device_name"]
    cl_path = config["device_class_path"]
    cl_type = config["device_class_type"]

srvr_addr = "tango://"+host+":"+port+"/"

if args.nodb:
    dev_name = srvr_addr + dev_name + "#dbase=no"

elif args.test:
    class_name = cl_path[cl_path.find("/") + 1: -3]
    dev_name = "test/nodb/" + class_name.lower()
    dev_name = srvr_addr + dev_name + "#dbase=no"

# Use PyTango
print("Tango version:", tango.__version__)
print("TANGO Database address:", tango.ApiUtil.get_env_var("TANGO_HOST"))

# Do client things
print("Connect to:", dev_name)
test_device = tango.DeviceProxy(dev_name)
print("Ping device:", test_device.ping(), "us")
print("The device state is:", test_device.state())
print("Defined attributes:", test_device.get_attribute_list())
print("Defined commands:", test_device.get_command_list())

if args.nodb or args.test:
    print("Defined properties:", "Unavailable for no database server")
else:
    print("Defined properties:", test_device.get_property_list("*"))

# Do more client things
if args.add:
    print("")
    print("Enable additional complexity - Do something crazy")
    print("Read:", test_device.dummy_measure_1)
