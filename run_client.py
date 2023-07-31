"""Command line Tango Device Client"""
from __future__ import print_function
from builtins import open
import argparse
import json
import socket
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
    cl_path = config["device_class_path"]
    dsr_name = config["device_server_name"]
    dev_name = config["device_name"]

if args.nodb:
    hostname = socket.gethostname() + ":8888/"
    nodb_name = "nodb/" + dev_name[dev_name.find("/") + 1:]
    dev_name = hostname + nodb_name + "#dbase=no"
elif args.test:
    ADDRESS = "tango://127.0.0.1:8888"
    class_name = cl_path[cl_path.find("/") + 1: -3]
    test_name = "/test/nodb/" + class_name
    dev_name = ADDRESS + test_name + "#dbase=no"
    print(dev_name)

# Do client things
print("Tango version:", tango.__version__)
print("TANGO Database address:", tango.ApiUtil.get_env_var("TANGO_HOST"))

test_device = tango.DeviceProxy(dev_name)
print("Ping device:", test_device.ping(), "us")
print("The device state is:", test_device.state())
print("Defined attributes:", test_device.get_attribute_list())
print("Defined commands:", test_device.get_command_list())

if args.nodb or args.test:
    print("Defined properties:", "Unavailable for no database server")
else:
    print("Defined properties:", test_device.get_property_list("*"))

if args.add:
    print("")
    print("Enable additional complexity - Do something crazy")
    print("Read voltage:", test_device.voltage)
