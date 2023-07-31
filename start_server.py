"""Command line tool to start a Tango Device Server"""
from __future__ import print_function
from builtins import open
import argparse
import os
import json

# Process command line arguments
parser = argparse.ArgumentParser(description="Starts a Tango Device Server")
parser.add_argument(
    "--nodb", help="Run device server without a database", action="store_true"
)
parser.add_argument(
    "--test", help="Run test device server (no database)", action="store_true"
)
args = parser.parse_args()

# Process config file
with open("config/config.json", "r", encoding="utf-8") as config_file:
    config = json.load(config_file)
    cl_path = config["device_class_path"]
    dsr_name = config["device_server_name"]
    dev_name = config["device_name"]

# Start device server: Python <Server_file>.py <instance name>
if args.nodb:
    command = "python " + cl_path + " test "
    ADDRESS = "--port 8888 "
    OPTIONS = "--nodb --dlist "
    nodb_name = "nodb/" + dev_name[dev_name.find("/") + 1:] + " "
    print("Start no db device server with device:", nodb_name)
    os.system(command + OPTIONS + nodb_name + ADDRESS)

elif args.test:
    COMMAND = "python -m tango.test_context "
    class_name = cl_path[cl_path.find("/") + 1: -3]
    python_path = cl_path[: cl_path.find("/")] + 2 * ("." + class_name) + " "
    ADDRESS = "--host 127.0.0.1 "
    os.system(COMMAND + python_path + ADDRESS)

else:
    command = "python " + cl_path + " test "
    print("Start device server")
    os.system(command)
