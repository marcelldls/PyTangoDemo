"""Command line Tango Device Client"""
import argparse
import tango
from src.utils import config_parse

# Process command line arguments
parser = argparse.ArgumentParser(description="Run a Tango Client")
parser.add_argument(
    "deviceConfig",
    help="Specify a device configuration",
)
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
cnfg = config_parse(args.deviceConfig)

srvr_addr = "tango://"+cnfg.host+":"+cnfg.port+"/"

if args.nodb:
    cnfg.dev_name = srvr_addr + cnfg.dev_name + "#dbase=no"

elif args.test:
    class_name = cnfg.cl_path[cnfg.cl_path.find("/") + 1: -3]
    cnfg.dev_name = "test/nodb/" + class_name.lower()
    cnfg.dev_name = srvr_addr + cnfg.dev_name + "#dbase=no"

# Use PyTango
print("Tango version:", tango.__version__)
print("TANGO Database address:", tango.ApiUtil.get_env_var("TANGO_HOST"))

# Do client things
print("Connect to:", cnfg.dev_name)
test_device = tango.DeviceProxy(cnfg.dev_name)
print("Ping device:", test_device.ping(), "us")
print("The device state is:", test_device.state())
attributes = test_device.get_attribute_list()
print("Defined attributes:", attributes)
print("Attribute values:",
      [test_device.read_attribute(att).value for att in attributes])
print("Defined commands:", test_device.get_command_list())

if args.nodb or args.test:
    print("Defined device properties:", "Unavailable for no database server")
else:
    print("Defined device properties:", test_device.get_property_list("*"))
    test_device.get_property_list("*")

# Do more client things
if args.add:
    print("")
    print("Enable additional complexity - Do something crazy")
    print("Read:", test_device.dummy_measure_1)
